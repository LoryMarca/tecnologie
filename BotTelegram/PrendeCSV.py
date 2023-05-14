from database import database
import DataBenzinaio as benz
import csv
import requests


urlBenzinai = 'https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv' #url del file dei benzinai
urlPrezzi = 'https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv' #url del file dei prezzi
filecsvBenzinai = 'BotTelegram/files/datiBenzinai.csv'
filecsvPrezzi = 'BotTelegram/files/datiPrezzi.csv'

class PrendeCSV:#classe per la lettura del file csv
        
        
    def scaricaDati():
        
        datiBenzinai = requests.get(urlBenzinai)
        if datiBenzinai.status_code == 200:
            with open(filecsvBenzinai, 'w') as f:
                f.write(datiBenzinai.content.decode('utf-8'))
        
        datiPrezzi = requests.get(urlPrezzi)        
        if datiPrezzi.status_code == 200:
           with open(filecsvPrezzi, 'w') as f:
                f.write(datiPrezzi.content.decode('utf-8'))


        
        
    def get_data_benzinai():
        with open(filecsvBenzinai, mode='r') as csv_file:
            next(csv_file)# skip header
            csv_reader = csv.DictReader(csv_file, delimiter=';')# lettura del file
            
            list = []
            
            for row in csv_reader:# lettura del file
                list.append(row)#aggiunta dei dati in una lista
                
            return list
        
    def get_data_prezzi():
        with open(filecsvPrezzi, mode='r') as csv_file:
            next(csv_file)# skip header
            csv_reader = csv.DictReader(csv_file, delimiter=';')# lettura del file
            
            list = []
            
            for row in csv_reader:# lettura del file
                list.append(row)#aggiunta dei dati in una lista
                
            return list
