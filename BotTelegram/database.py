import mysql.connector

class database:#creazione della connessione al database

    def __init__(self, ip, username, password, nome_database):
        self.database = mysql.connector.connect(host=ip, user=username, password=password, database=nome_database)
        self.cursor = self.database.cursor()
        print(self.database.get_server_info())
    
    def getDatabase(self):
        return self.database
    
    def getCursor(self):
        return self.cursor