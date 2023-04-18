import sqlite3 as sql

class db:#creazione della connessione al database
    def get_conn() -> sql.Connection:
        conn = sql.connect("C:\Users\lorym\Desktop\SCUOLA\TECNOLOGIA\GitHub\tecnologie\progettoBenza\DAtaBAse.db")
        return conn
