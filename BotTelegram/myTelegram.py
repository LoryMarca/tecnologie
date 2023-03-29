import requests


class myTelegram:
    def __init__(self,token):
        self.TOKEN=token
        self.URL=f"https://api.telegram.org/bot{self.TOKEN}/"
        self.servizio="getUpdates"
        self.servizioSand="sendMessage"
        self.result=requests.get(self.URL+self.servizio)
        if self.result.status_code==200:
            self.dato=self.result.json()
            if self.dato["ok"]:
                for messaggio in self.dato["result"]:
                    if (str(messaggio["message"]["text"]).lower().find("lagre è ghei")!=-1):
                        # rispondi
                        text="vero"
                        chatID=messaggio["message"]["chat"]["id"]
                        
                        print(text)
                        print(chatID)
                        
                        requests.get(self.URL+self.servizioSand,params={"chat_id":chatID,"text":text})
                        
                        self.result=requests.get(self.URL+self.servizio,params={"offset":self.dato["result"][-1]})
            
                        
    def getUpdates(self):
    
    def sendMessage(self):
    
    def start(self):
    
    def echo(self):
    
    def image(self):
    
    def getUpdates(self):
    
    def sendMessage(self):
    
    def start(self):
    
    def echo(self):
    
    def image(self):
    
    def getUpdates(self):