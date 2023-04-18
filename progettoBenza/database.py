import sqlite3 as sql3

class database:#creazione della connessione al database
    global conn#creazione della connessione al database
    def connect()->sql3.Connection:#apertura della connessione
        conn= sql3.connect("__database__.db")
    def close()->sql3.Connection:#chiusura della connessione
        conn.close()
        
    def execute(query, params):#esecuzione della query
        conn.execute(query, parameters=params)
        conn.commit()
        
    

    
    
