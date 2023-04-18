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

    def __str__(self):#struttura della classe
        return f"ID Benzinaio: {self.idBenzinaio}\nGestore: {self.Gestore}\nBandiera: {self.Bandiera}\nTipo Benzinaio: {self.TipoBenzinaio}\nNome Benzinaio: {self.NomeBenzinaio}\nIndirizzo: {self.Indirizzo}\nComune: {self.Comune}\nProvincia: {self.Provincia}\nLatitudine: {self.Latitudine}\nLongitudine: {self.Longitudine}"

    def modifica_indirizzo(self, nuovo_indirizzo):#modifica dell'indirizzo
        self.Indirizzo = nuovo_indirizzo

    def modifica_gestore(self, nuovo_gestore):#modifica del gestore
        self.Gestore = nuovo_gestore

    def modifica_bandiera(self, nuova_bandiera):#modifica della bandiera
        self.Bandiera = nuova_bandiera
