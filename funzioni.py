import dati

################## SEZIONE PRODUZIONE LATTE #####################################
############## ############ ############# ############### ################# ##############
#Composizione Bestiame / Produzione latte annuale in KG
Bestiame = {"A":10977, "B":7425, "C":7415}
#quanto latte produco al giorno?
#Creo un nuovo dizionario, in cui ci metto i valori divisi per 305
Bestiame_litri_giorno = {}
for razza,litri in Bestiame.items():
    Bestiame_litri_giorno[razza] = litri / dati.mucca_lattazione

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



################## SEZIONE PASTORIZZAZIONE DEL LATTE #####################################
############## ############ ############# ############### ################# ##############

#Mi dice quanto latte pastorizzo considerando lo scarto di lavorazione di 5%
def Pastorizzazione(litriLatte):
    scarto = 0.05 #supponiamo che il 5% del latte lo perdiamo
    scarto_litri = litriLatte * scarto
    litri_effettivi_pastorizzati = litriLatte - scarto_litri
    return litri_effettivi_pastorizzati

#Consumo elettrico della vasca da 300 Litri
def ConsumoElettricoPastorizzazione(numero_vasche,giorni):
    consumo_kw_ore_di_lavoro = dati.ore_lavoro_vasche_giorno * dati.consumo_vasca_KWh * numero_vasche * giorni
    Costo_totale = consumo_kw_ore_di_lavoro * dati.costo_kwh_medio
    return giorni,dati.ore_lavoro_vasche_giorno,consumo_kw_ore_di_lavoro,Costo_totale
#Quanto latte al giorno riesco a pastorizzare ?
#Cosa mi serve sapere per capire quanto posso pastorizzare ? Il tempo è ininfluente perchè ci vogliono pochi secondi
#Quello che fa la differenza è : 

#LATTE PRODOTTO AL GIORNO
def prod_latte_giorno(latte_A,latte_B,mandria_A,mandria_B):
    prod_latte_A = latte_A * mandria_A
    prod_latte_B = latte_B * mandria_B
    tot_prod_latte_giorno = prod_latte_A + prod_latte_B
    return tot_prod_latte_giorno

latte_A= Bestiame_litri_giorno["A"]
latte_B= Bestiame_litri_giorno["B"]
mandria_A= dati.mandria_A
mandria_B= dati.mandria_B

latte_totale_giorno = prod_latte_giorno(latte_A,latte_B,mandria_A,mandria_B)
print(f"{latte_totale_giorno:.2f} Litri/Giorno")

#CAPACITA MASSIMA DI PASTORIZZAZIONE
# Quante vasche ho / Quanta capacità di pastorizzazione hanno / Quante ore al giorno funzionano / Tolgo lo scarto 
numero_vasche = dati.numero_vasche_pastorizzazione 
capacità_vasca = dati.capacita_vasca 
ore_funzionamento = dati.ore_lavoro_vasche_giorno 
scarto_pastorizzazione = dati.scarto_pastorizzazione 
quanti_giorni = dati.stima_su_quanti_giorni 
#numero vasche * capacità * ore di funzionamento = capacità totale al giorno
#calcolo 5% della "capacità totale al giorno"
#Faccio la differenza tra lo scarto e capacità totale al giorno
def collo_bottigli_pastorizzazione_giorno(numeroVasche,capacitaVasca,oreFunzionamento,scarto,giorniLavorazione):
    capacità_totale = numeroVasche * capacitaVasca * oreFunzionamento * giorniLavorazione
    scarto_lavorazione = scarto * capacità_totale
    capacità_totale_reale = capacità_totale - scarto_lavorazione
    return capacità_totale_reale

pastorizzazione_reale_giorno_totale = collo_bottigli_pastorizzazione_giorno(numero_vasche,capacità_vasca,ore_funzionamento,scarto_pastorizzazione,quanti_giorni)
print(pastorizzazione_reale_giorno_totale)

# come creare la capacità massima di pastorizzazione giornaliera
# latte_prodotto_giorno
# capacita_pastorizzazione_giorno




#Prossimi step
#1) Calcola la produzione giornaliera di latte per 1 mucca (per tipo A/B/C)- FATTO
#2) CALCOLO CAPACITà MASSIMA DI PRODUZIONE LATTE PASTORIZZATO- FATTO
#3) CALCOLO LA CAPACITà CONSIDERANDO UNO SCARTO DI LAVORAZIONE- FATTO

#Definisco 3 output attesi dal programma 
#Latte intero / Yogurt / Formaggio Stagionato
# Latte: mungitura → trattamento/pastorizzazione → confezionamento
# Yogurt: mungitura → pastorizzazione → fermentazione → confezionamento
# Formaggio: mungitura → cagliata → salatura → stagionatura → confezionamento
