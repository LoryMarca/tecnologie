import requests


class myTelegram:
    def __init__(self,token):
        self.TOKEN=token
        self.URL=f"https://api.telegram.org/bot{self.TOKEN}/"
        self.servizio="getUpdates"
        self.servizioSand="sendMessage"
        
            
                        
    def getUpdates(self):
        
        output = []
        result=requests.get(self.URL+"getUpdates")
        
        if result.status_code==200:
            dato=result.json()
            
            if dato["ok"]:
                
                if len(dato["result"] > 0):
                    for messaggio in dato["result"]:
                        output.append(messaggio)
                    lastUpdateId = dato["result"][-1]["update_id"]
                    requests.get(self.URL+"getUpdates", params={"offset":lastUpdateId})     
           
                
                    
        return output
        """
        if (str(messaggio["message"]["text"]).lower().find("ciao")!=-1):
            # rispondi
            text="vero"
            chatID=messaggio["message"]["chat"]["id"]
            
            print(text)
            print(chatID)
            
            result=requests.get(self.URL+self.servizio,params={"offset":dato["result"][-1]})"""

    def sendMessage(self, chat_id, messaggio):
        response = requests.get(self.URL+'sendMessage',params={"chat_id":chat_id,"text":messaggio})
        return response
        
    def start(self):
        pass
    def echo(self):
        pass
    def image(self):
        pass
    def getUpdates(self):
        pass
    def sendMessage(self):
        pass
    def start(self):
        pass
    def echo(self):
        pass
    def image(self):
        pass
s