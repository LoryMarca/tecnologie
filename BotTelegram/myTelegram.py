import requests
import PrendeCSV
from database import database
import math


class myTelegram:
    def __init__(self,token):#inizializzazione del bot
        self.TOKEN=token
        self.URL=f"https://api.telegram.org/bot{self.TOKEN}/"
        self.servizio="getUpdates"
        self.servizioSand="sendMessage"
        self.database = database('localhost', 'root', '', 'botelegram')
        
            
                        
    def getUpdates(self):#funzione per leggere i messaggi
        
        output = []
        result=requests.get(self.URL+"getUpdates")
        
        if result.status_code==200:
            dato=result.json()
            
            if dato["ok"]:
                
                if len(dato["result"])  > 0:
                    for messaggio in dato["result"]:
                        output.append(messaggio)
                        print(messaggio)
                        
                    lastUpdateId = dato["result"][-1]["update_id"]
                    requests.get(self.URL+"getUpdates", params={"offset":lastUpdateId+1})     
           
                
                    
        return output
        """
        if (str(messaggio["message"]["text"]).lower().find("ciao")!=-1):
            # rispondi
            text="vero"
            chatID=messaggio["message"]["chat"]["id"]
            
            print(text)
            print(chatID)
            
            result=requests.get(self.URL+self.servizio,params={"offset":dato["result"][-1]})"""

    def sendMessage(self, chat_id, messaggio):#funzione per inviare i messaggi
        response = requests.get(self.URL+'sendMessage',params={"chat_id":chat_id,"text":messaggio})
        return response
        
    def start(self):
        pass
    def echo(self):
        pass
    def image(self):
        pass
    
    
    def CaricaDati(self):#carica i dati sul db
        PrendeCSV.PrendeCSV.scaricaDati()
        db = self.database.getDatabase()#connessione al db
        cursore = self.database.getCursor()
        dataBenzinai = PrendeCSV.PrendeCSV.get_data_benzinai()#carica i dati
        for benzinaio in dataBenzinai:
            
            for key in benzinaio.keys():#elimina le virgole
                benzinaio[key] = str(benzinaio[key]).replace('"','')
            
            sql = f"""INSERT IGNORE INTO impianti (idImpianto, Gestore, TipoImpianto, NomeImpianto, Indirizzo, Comune, Provincia, Latitudine, Longitudine) VALUES ("{benzinaio['idImpianto']}", "{benzinaio['Gestore']}", "{benzinaio['Tipo Impianto']}", "{benzinaio['Nome Impianto']}", "{benzinaio['Indirizzo']}", "{benzinaio['Comune']}", "{benzinaio['Provincia']}", "{benzinaio['Latitudine']}", "{benzinaio['Longitudine']}")"""            
            cursore.execute(sql)#inserisce i dati
        db.commit()
        print('Impianti caricati')
        
        #mo fa le stessa cosa ma per i prezzi
        dataPrezzi = PrendeCSV.PrendeCSV.get_data_prezzi()
        for prezzo in dataPrezzi:
            
            for key in prezzo.keys():
                prezzo[key] = str(prezzo[key]).replace('"','')
            
            sql = f"""INSERT IGNORE INTO prezzi (idImp, descCarburante, prezzo, isSelf) VALUES ("{prezzo['idImpianto']}", "{prezzo['descCarburante']}", "{prezzo['prezzo']}", "{prezzo['isSelf']}")"""            
            cursore.execute(sql)
        db.commit()
        print('Prezzi caricati')
                
        
    def processaMessaggio(self, messaggio):#vede che messaggio c'è e fa cose in base ad esso
        chatID=messaggio["message"]["chat"]["id"]
        database = self.database.getDatabase()
        cursore = database.cursor()
        
        message_text = ''
        if 'text' in messaggio["message"]:
            message_text = messaggio["message"]["text"]
        
 
        if message_text == "/start":#qua salva l'utente(dato che botfather chiede lui direttamente lo /start per iniziare il bot no serve scriverlo due volte ma legge direttamente quello)
            sql = f"""INSERT INTO utente (user, chatID) VALUES ("{messaggio['message']["from"]["username"]}", "{chatID}")"""
            cursore.execute(sql)
            database.commit()
            
        elif message_text == "/getbenzinai":#dopo questo comando il bot ti chiederà di invialgli la posizione
            sql =f"UPDATE utente SET stato='richiediPosizione' WHERE chatID LIKE '{chatID}'"        
            cursore.execute(sql)
            database.commit()
            self.sendMessage(chatID, "Invia la tua posizione")
            pass
            
            
        else:
            print('Non è un comando')
            statoUtente = ''
            
            cursore.execute(f"SELECT stato FROM utente WHERE chatID LIKE '{messaggio['message']['chat']['id']}'")
            result = cursore.fetchall()
            if result != None:
                if len(result) > 0:
                    statoUtente = result[0][0]
            
            print(f'statoUtente: "{statoUtente}"')
            
            if statoUtente == 'richiediPosizione' :
               if 'location' in messaggio["message"]:
                    cursore.execute(f"SELECT * FROM impianti")
                    impianti = cursore.fetchall()
                    benzinaiVicini = []
                    distanza = 3
                    origin_latitude = messaggio["message"]["location"]["latitude"]
                    origin_longitude = messaggio["message"]["location"]["longitude"]
                    
                    for benzinaio in impianti:
                        d = self.distance(origin_latitude, origin_longitude, benzinaio[8], benzinaio[9])
                        if d <= distanza:
                            benzinaiVicini.append({'benzinaio':benzinaio, 'distanza':round(d,2)})

                    print(f'trovati {len(benzinaiVicini)} benzinai vicini')                    
                    benzinaiVicini.sort(key=lambda x: x['distanza'])
                    
                    i = 0
                    while i < 5 and i < len(benzinaiVicini):
                        self.sendMessage(chatID, f'Benzinaio vicino: {benzinaiVicini[i]["benzinaio"][1]} - {benzinaiVicini[i]["distanza"]} km')
                        i += 1
                        
                    
                    sql = f'UPDATE utente SET stato=NULL WHERE chatID LIKE "{chatID}"'
                    cursore.execute(sql)
                    database.commit()
            
            else:
                self.sendMessage(chatID, "Nessun comando")
        pass
    
    
    
    
    def distance(self, lat1, lon1, lat2, lon2):
        R = 6371  # radius of the Earth in kilometers

        # convert latitude and longitude to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # calculate the differences between the latitudes and longitudes
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # apply the Haversine formula to calculate the distance
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        return distance