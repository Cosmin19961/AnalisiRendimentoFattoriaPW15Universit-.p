#PRODUZIONE MEDIA LATTE DI UNA MUCCA
latteMedioGiorno = 40
latteMedioGiornoInCondizioniScarse = 20

#PRODUZIONE MEDIA ANNUA LATTE PER RAZZA DI MUCCA IN ITALIA
Frisona_Italiana = 10386 / 305 #Calcolo meedia giornaliera / Si divide per 305 perchè una mucca produce latte per circa 305 giorni l'anno
Bruna_Alpina = 7661 / 305
pezzata_Rossa_Italiana = 7146 / 305
Jersey = 6781 / 305
#Creo un dizionario con queste chiavi e valori
produzioneMediaAnnuaLattePerRazza = {
    "Frisona_Italiana": Frisona_Italiana,
    "Bruna_Alpina": Bruna_Alpina,
    "Pezzata_Rossa_Italiana": pezzata_Rossa_Italiana,
    "Jersey": Jersey
}

for razza,produzione in produzioneMediaAnnuaLattePerRazza.items():
    print(razza,f"{produzione:.2f}","Litri/Giorno")
#Genero una lista con l'eta minima e massima di vita della mucca

#Da rivedere
#Generatore di vita, quando l'oggetto MUCCA nasce, deve avere assegnato questa variabile, in modo che so quanto vivrà 
generatoreCasualeEta = random.randint(1,15) #Generatore in ANNI
generatoreCasualeEtaGiorni = generatoreCasualeEta * 365 #Generatore in giorni

#genera una lista dei giorni casuali basata su quella precedente
scorrereGiorniDiVita = list(range(1,generatoreCasualeEtaGiorni +1))

#prendo in esame il massimo giorno di vita generato
GiornoMassimoDiVita = scorrereGiorniDiVita[-1]

#moltiplico i giorni di vita * produzione latte media
ProduzioneMassimaLatteSuVitaMassimaStandard = GiornoMassimoDiVita * latteMedioGiorno

#produzione latte media annuale
ProduzioneMediaLatteSuVitaMassimaStandardAnnuale = ProduzioneMassimaLatteSuVitaMassimaStandard / generatoreCasualeEta 
#Produzione latte media mensile
ProduzioneMediaLatteSuVitaMassimaStandardMensile = ProduzioneMassimaLatteSuVitaMassimaStandard / generatoreCasualeEta / 12 

print(f"La mucca ha vissuto per {generatoreCasualeEta} anni, equivalenti a {generatoreCasualeEtaGiorni} giorni")
print(f"Produzione latte vita intera {ProduzioneMassimaLatteSuVitaMassimaStandard}")
print(f"Produzione latte media annuale:{ProduzioneMediaLatteSuVitaMassimaStandardAnnuale}")
print(f"Produzione latte media mensile:{ProduzioneMediaLatteSuVitaMassimaStandardMensile}")
