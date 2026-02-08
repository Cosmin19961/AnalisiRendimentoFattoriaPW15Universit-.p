import dati

#Composizione Bestiame / Produzione latte annuale in KG
Bestiame = {"Frisona":10977, "Bruna":7425, "Pezzata":7415}

#Conversione litri / kg
def conversioneLitri (quantitaDaConvertire):
    IndiceDiConversione = 1.03
    totaleLitri = quantitaDaConvertire / IndiceDiConversione
    return totaleLitri

#Conversione LITRI a KG
def conversioneKg(quantitaDaConvertire):
    IndiceDiConversione = 1.03
    totaleKg = IndiceDiConversione * quantitaDaConvertire
    return totaleKg

#Definisco 3 output attesi dal programma 
#Latte intero / Yogurt / Formaggio Stagionato
# Latte: mungitura → trattamento/pastorizzazione → confezionamento
# Yogurt: mungitura → pastorizzazione → fermentazione → confezionamento
# Formaggio: mungitura → cagliata → salatura → stagionatura → confezionamento

#quanto latte produco al giorno?
def LitriAlGiorno(litri_annuali):
    latte_giornaliero = litri_annuali / 305
    return latte_giornaliero
#Quanto dura il trattamento / pastorizzazione ?



################## SEZIONE PASTORIZZAZIONE DEL LATTE #####################################
############## ############ ############# ############### ################# ##############

#Mi dice quanto latte pastorizzo considerando lo scarto di lavorazione di 5%
def Pastorizzazione(litriLatte):
    scarto = 0.05 #supponiamo che il 5% del latte lo perdiamo
    scarto_litri = litriLatte * scarto
    litri_effettivi_pastorizzati = litriLatte - scarto_litri
    return litri_effettivi_pastorizzati

#modello ti dipo : VASCA 300/L H
def ConsumoElettricoPastorizzazione(numero_vasche,giorni):
    consumo_kw_ore_di_lavoro = dati.ore_lavoro_vasche_giorno * dati.consumo_vasca_KWh * numero_vasche * giorni
    kWh_totali = consumo_kw_ore_di_lavoro * dati.costo_kwh_medio
    kWh_totali_giorni_utilizzo = kWh_totali 
    return dati.stima_su_quanti_giorni,dati.ore_lavoro_vasche_giorno,consumo_kw_ore_di_lavoro,kWh_totali

print(ConsumoElettricoPastorizzazione(dati.numero_vasche_pastorizzazione,dati.stima_su_quanti_giorni))

#Quanto dura il confezionamento ?
#Obiettivo sapere quanti latte pastorizzato ottengo in 365 giorni x una mucca
