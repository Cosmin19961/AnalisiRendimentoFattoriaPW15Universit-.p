import CostantiVariabili

#Definisco la classe MUCCA
class Mucca():
    def __init__(self,razza,eta,gradivanza,qualitàNutrizione): 
        self.razza = razza
        self.eta = eta
        self.gradivanz = gradivanza
        self.qualitàNutrizione = qualitàNutrizione
    #Stima della produzione del latte giornaliero
    def produzioneLatte(self):
        #Controllo l'età della mucca per stabilire la produzione media di latte
        #Queste condizioni si applicano alla mucca in perfetta salute / ben nutrita / subito dopo il parto (quindi massima lattazione)
         #PRODUZIONE GIORNALIERA LATTE IN BASE ALLA RAZA
        
            if self.razza in CostantiVariabili.produzioneMediaAnnuaLattePerRazza:
                produzioneLatte = CostantiVariabili.produzioneMediaAnnuaLattePerRazza[self.razza]
                print(f"Litri x {produzioneLatte:.2f}")
        #Se la razza della mucca non è indicata nel dizionario, si applica la produzione media giornaliera standard
            else:
                if  self.gradivanz == False and self.qualitàNutrizione == True: #Imposto la gravidanza False (quindi non è incinta ma appena partorito) e la qualità del cibo su buon (true)
                    if self.eta <= 5:
                        CostantiVariabili.latteMedioGiorno = 50
                    elif self.eta >= 10:
                        CostantiVariabili.latteMedioGiorno = 10
                    elif self.eta > 5:
                        CostantiVariabili.latteMedioGiorno = 25
                    produzioneLatte = CostantiVariabili.latteMedioGiorno
                else:
                    produzioneLatte = CostantiVariabili.latteMedioGiornoInCondizioniScarse
                print(f"Litri latte munto al giorno {produzioneLatte}")           
    def __str__(self):
        return f"RAZZA {self.razza} ETA {self.eta} GRADIVANZA {self.gradivanza}"
 
mucca1 = Mucca("Piemontese",10,False,True)
mucca1.produzioneLatte()

