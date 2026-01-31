
#Definisco la classe MUCCA
class Mucca():
    def __init__(self,razza,eta,peso,stambulazione_fissa,stambulazione_libera,parto,tempo_stambulazione_fissa,stato_salute,alimentazione): 
        self.razza = razza
        self.eta = eta
        self.peso = peso
        self.stambulazione_fissa = stambulazione_fissa #Vive in Stalla perenne (può influire sulla produzione di latte)
        self.stambulazione_libera = stambulazione_libera #Vive all'aperto per più del 50% del giorno
        self.parto = parto #Solo se ha partorito una volta è considerata una mucca
        self.tempo_stambulazione_fissa = stambulazione_fissa #Max 14 giorni legate in stalla al loro posto
        self.stato_salute = stato_salute #punteggio da 1 a 10
        self.alimentazione = alimentazione #che tipo di fieno mangia
    def __str__(self):
        return f"Ancora da inizializzare"
 
mucca1 = Mucca("Piemonetese",5,450,False,True,True,10,9,"PrimoTaglio")
print(mucca1)
