#Produzione latte / pastorizzazione latte
# latte_pastorizzato_produzione_latte.py
import dati
from report import stampa_report  #hocambiato

################## SEZIONE PRODUZIONE LATTE #####################################
############## ############ ############# ############### ################# ##############
# L/Anno
Bestiame = {"A":10977, "B":7425, "C":7415}

# L / Giorno
Bestiame_litri_giorno = {}
for razza,litri in Bestiame.items():
    Bestiame_litri_giorno[razza] = litri / dati.mucca_lattazione

################## SEZIONE PASTORIZZAZIONE DEL LATTE #####################################
############## ############ ############# ############### ################# ##############

#Mi dice quanto latte pastorizzo considerando lo scarto di lavorazione di 5%
""" def Pastorizzazione(litriLatte):
    scarto = 0.05 #supponiamo che il 5% del latte lo perdiamo
    scarto_litri = litriLatte * scarto
    litri_effettivi_pastorizzati = litriLatte - scarto_litri
    return litri_effettivi_pastorizzati #Mi ritorna i litri effettivi di latte pastorizzato
 """
#Consumo elettrico della vasca da 300 Litri
def ConsumoElettricoPastorizzazione(numero_vasche,giorni):
    consumo_kw_ore_di_lavoro = dati.ore_lavoro_vasche_giorno * dati.consumo_vasca_KWh * numero_vasche * giorni
    Costo_totale = consumo_kw_ore_di_lavoro * dati.costo_kwh_medio
    return giorni,dati.ore_lavoro_vasche_giorno,consumo_kw_ore_di_lavoro,Costo_totale

#LATTE PRODOTTO AL GIORNO
def prod_latte_giorno(latte_A,latte_B,mandria_A,mandria_B,scarto_mungitura,scarto_macchinari):
    tot_prod_latte_giorno = (latte_A * mandria_A) + (latte_B * mandria_B)
    tot_scarto = (scarto_mungitura + scarto_macchinari) * tot_prod_latte_giorno
    tot_latte_realistico_giorno = tot_prod_latte_giorno - tot_scarto
    return tot_prod_latte_giorno,tot_latte_realistico_giorno

#CAPACITA MASSIMA DI PASTORIZZAZIONE
def collo_bottigli_pastorizzazione_giorno(numeroVasche,capacitaVasca,oreFunzionamento):
    capacità_totale = numeroVasche * capacitaVasca * oreFunzionamento
    return capacità_totale

def run():  #hocambiato
    latte_A= Bestiame_litri_giorno["A"] #Prendo i litri di latte generati dai capi A dal dizionario 
    latte_B= Bestiame_litri_giorno["B"] #Prendo i litri di altte generati dai capi B dal dizionario
    mandria_A= dati.mandria_A #Prendo da DATI la quantità di capi A
    mandria_B= dati.mandria_B #Prendo da DATI la quantità di capi B
    scarto_mungitura = dati.scarto_mungitura #Importo da dati lo scarto della mungitura
    scarto_macchinari = dati.scarto_macchinari #Importo da dati lo scarto generato dai macchinari

    numero_vasche = dati.numero_vasche_pastorizzazione
    capacità_vasca = dati.capacita_vasca
    ore_funzionamento = dati.ore_lavoro_vasche_giorno

    pastorizzazione_reale_giorno_totale = collo_bottigli_pastorizzazione_giorno(numero_vasche,capacità_vasca,ore_funzionamento)

    #ECCESSO DI PRODUZZIONE vs CAPACITà DI PASTORIZZAZIONE
    latte_giornaliero_atteso,latte_giornalieto_munto = prod_latte_giorno(latte_A,latte_B,mandria_A,mandria_B,scarto_mungitura,scarto_macchinari)
    capacita_massima_past_giorno = collo_bottigli_pastorizzazione_giorno(numero_vasche,capacità_vasca,ore_funzionamento)#qui metto la capacità massima di pastorizzazione

    latte_avanzato = 0
    latte_pastorizzato = 0
    if(latte_giornalieto_munto > capacita_massima_past_giorno):
        latte_avanzato = latte_giornalieto_munto - capacita_massima_past_giorno
        latte_pastorizzato = capacita_massima_past_giorno
    else:
        latte_pastorizzato = latte_giornalieto_munto

    #Se vendo yogurt, allora devo considerare i litri di latte totali che destinerò allo yogurt e venderò la rimanenza
    #Blocco da finire
    flag_report_pastorizzazione = dati.flag_pastorizzazione
    if flag_report_pastorizzazione == True: #Se l'interuttore è "acceso"
        ########.   REPORT SEZIONE PASTORIZZAZIONE LATTE E VENDITA / ANCHE SUL CRUDO .####################
        stampa_report("capacita_massima_pastorizzazione", pastorizzazione_reale_giorno_totale=pastorizzazione_reale_giorno_totale) #Quanti litri posso pastorizzare totale
        stampa_report("scarto_mungitura", scarto_mungitura_percent=dati.scarto_mungitura * 100)  #Mi da lo scarto della mungitura
        stampa_report("scarto_macchinari", scarto_macchinari_percent=dati.scarto_macchinari * 100) #Mi da lo scarto dei macchinari
        #Latte torico (senza scarto)
        stampa_report("latte_munto_atteso", latte_giornaliero_atteso=latte_giornaliero_atteso)  #Mi da il latte che spero di ottenere
        stampa_report("latte_pastorizzato_effettivo", latte_pastorizzato=latte_pastorizzato)  #Mi da il latte che ottengo effettivamente
        #Latte munto con lo scarto
        stampa_report("latte_non_pastorizzato", latte_avanzato=latte_avanzato)  
        vendita_latte_crudo = latte_avanzato * dati.prezzo_latte_crudo #Vendo il latte crudo * il prezzo del latte crudo importato da dati
        stampa_report("ricavo_latte_crudo", vendita_latte_crudo=vendita_latte_crudo)  #mando a schermo il ricavo del latte crudo
        vendita_latte_pastorizzato = latte_pastorizzato * dati.prezzo_latte_pastorizzato #Vendo il latte pastorizzato effettivamente * il prezzo del latte pastorizzato da dati
        stampa_report("ricavo_latte_pastorizzato", vendita_latte_pastorizzato=vendita_latte_pastorizzato)  #Mando a schermo il ricavo totale del latte pastorizzato
    else:
        pass

    return latte_pastorizzato  #Mi ritorna il latte pastorizzato in mood da poterlo utilizzare successivamente negli altri fogli per la produzione di yogurt e formaggio.