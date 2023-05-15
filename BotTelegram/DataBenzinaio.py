#in verità non serve questo file ma l'ho fatto quindi lo tengo :)

class DataBenzinaio:#classe per la lettura del file csv
    
    def __init__(self, idBenzinaio, Gestore, Bandiera, TipoBenzinaio, NomeBenzinaio, Indirizzo, Comune, Provincia, Latitudine, Longitudine):
        self.idBenzinaio = idBenzinaio
        self.Gestore = Gestore
        self.Bandiera = Bandiera
        self.TipoBenzinaio = TipoBenzinaio
        self.NomeBenzinaio = NomeBenzinaio
        self.Indirizzo = Indirizzo
        self.Comune = Comune
        self.Provincia = Provincia
        self.Latitudine = Latitudine
        self.Longitudine = Longitudine

    def toString(self):#struttura della classe
        return f"ID Benzinaio: {self.idBenzinaio}\nGestore: {self.Gestore}\nBandiera: {self.Bandiera}\nTipo Benzinaio: {self.TipoBenzinaio}\nNome Benzinaio: {self.NomeBenzinaio}\nIndirizzo: {self.Indirizzo}\nComune: {self.Comune}\nProvincia: {self.Provincia}\nLatitudine: {self.Latitudine}\nLongitudine: {self.Longitudine}"

    def modIndirizzo(self, nuovoIndirizzo):#modifica dell'indirizzo
        self.Indirizzo = nuovoIndirizzo

    def modGestore(self, nuovoGestore):#modifica del gestore
        self.Gestore = nuovoGestore

    def modBandiera(self, nuovaBandiera):#modifica della bandiera
        self.Bandiera = nuovaBandiera
