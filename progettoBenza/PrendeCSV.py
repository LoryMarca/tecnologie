from dataManager import get_conn
import DataBenzinaio as benz
import csv
import requests
from database import execute_query
url = "https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv" # url del file csv
filecsv = "database\\files\\filecsv.csv"# nome del file csv

class PrendeCSV:#classe per la lettura del file csv
        
    def get_data():
        with open(filecsv, mode='r', encoding='utf8') as csv_file:
            next(csv_file)# skip header
            csv_reader = csv.DictReader(csv_file, delimiter=';')# lettura del file
            
            for row in csv_reader:# lettura del file
                benzinaio = benz.benz(row['idImpianto'], row['Gestore'], row['Bandiera'], row['Indirizzo'],row['Comune'], row['Provincia'], row['Latitudine'], row['Longitudine'])
                list = list.append(benzinaio)#aggiunta dei dati in una lista
                
            return list
