import requests

TOKEN = "6131316606:AAEPAdSdE3cd0rTciMEDKSa5zUxQvlLlHks"
URL = f"https://api.telegram.org/bot{TOKEN}/"# se si mette la "f" davanti possiamo mettere le variabili nelle graffe


servizio = "getUpdates"
servizioSand = "sendMessage"
result = requests.get(URL+servizio)

if result.status_code == 200:
    dato = result.json()
    if dato["ok"]:
        for messaggio in dato["result"]:
            if (str(messaggio["message"]["text"]).lower().find("dambro napoletano") != -1):
                # rispondi
                text = "siiiii e down"
                chatID=messaggio["message"]["chat"]["id"]
                
                print(text)
                print(chatID)

                requests.get(URL+servizioSand,params={"chat_id":chatID,"text":text})
        
        result=requests.get(URL+servizio,params={"offset":dato["result"][-1]})
