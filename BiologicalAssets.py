import CostantiVariabili

#Definisco la classe MUCCA
class Mucca():
    def __init__(self,razza,eta,peso,stambulazione_libera,parto,stato_salute,alimentazione): 
        self.razza = razza
        self.eta = eta
        self.peso = peso
        self.stambulazione_libera = stambulazione_libera #Vive all'aperto per più del 50% del giorno
        self.parto = parto #Solo se ha partorito una volta è considerata una mucca
        self.stato_salute = stato_salute #punteggio da 1 a 10
        self.alimentazione = alimentazione #che tipo di fieno mangia
    #Stima della produzione del latte giornaliero
    def produzioneLatte(self):
        produzioneLatte = self.eta + CostantiVariabili.latteMedioGiorno
        print(f"Litri latte munto al giorno {produzioneLatte}")
    
    
    def __str__(self):
        return f"RAZZA {self.razza} ETA {self.eta} PESO {self.peso} LIBERA {self.stambulazione_libera} PARTO {self.parto} SALUTE {self.stato_salute} FIENO {self.alimentazione}"
 
mucca1 = Mucca("Piemontese",10,450,True,True,9,"INSERIRE TIPOFIENO")
mucca1.produzioneLatte()