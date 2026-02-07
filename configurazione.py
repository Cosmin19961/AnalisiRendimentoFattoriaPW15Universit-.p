#Giorni della simulazione
Giorno = 365

#Composizione Bestiame / Produzione latte annuale in KG
Bestiame = {"Frisona":10.977, "Bruna":7.425, "Pezzata":7.415}

#Conversione litri / kg
def conversioneLitri (quantitaDaConvertire):
    IndiceDiConversione = 1.03
    totaleLitri = quantitaDaConvertire / IndiceDiConversione
    return totaleLitri
KG = 1500
ottieni_litri = conversioneLitri(KG)
print(f"Hai {KG} kg che equivalgono a {ottieni_litri} litri")

#Conversione LITRI a KG
def conversioneKg(quantitaDaConvertire):
    IndiceDiConversione = 1.03
    totaleKg = IndiceDiConversione * quantitaDaConvertire
    return totaleKg

litri = 1456.3106796116504
ottieni_litri = conversioneKg(litri)
print(ottieni_litri)

#Definisco 3 output attesi dal programma 
#Latte intero / Yogurt / Formaggio Stagionato
# Latte: mungitura → trattamento/pastorizzazione → confezionamento
# Yogurt: mungitura → pastorizzazione → fermentazione → confezionamento
# Formaggio: mungitura → cagliata → salatura → stagionatura → confezionamento
