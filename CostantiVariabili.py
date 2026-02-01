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
