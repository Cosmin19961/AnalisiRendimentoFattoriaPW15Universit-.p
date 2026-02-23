import dati

################## SEZIONE PRODUZIONE LATTE #####################################
############## ############ ############# ############### ################# ##############
# L/Anno 
Bestiame = {"A":10977, "B":7425, "C":7415}

# L / Giorno
Bestiame_litri_giorno = {}
for razza,litri in Bestiame.items():
    Bestiame_litri_giorno[razza] = litri / dati.mucca_lattazione


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

#LATTE PRODOTTO AL GIORNO
def prod_latte_giorno(latte_A,latte_B,mandria_A,mandria_B,scarto_mungitura,scarto_macchinari):
    tot_prod_latte_giorno = (latte_A * mandria_A) + (latte_B * mandria_B)
    tot_scarto = (scarto_mungitura + scarto_macchinari) * tot_prod_latte_giorno
    tot_latte_realistico_giorno = tot_prod_latte_giorno - tot_scarto
    return tot_prod_latte_giorno,tot_latte_realistico_giorno

latte_A= Bestiame_litri_giorno["A"]
latte_B= Bestiame_litri_giorno["B"]
mandria_A= dati.mandria_A
mandria_B= dati.mandria_B
scarto_mungitura = dati.scarto_mungitura
scarto_macchinari = dati.scarto_macchinari

#CAPACITA MASSIMA DI PASTORIZZAZIONE
numero_vasche = dati.numero_vasche_pastorizzazione 
capacità_vasca = dati.capacita_vasca 
ore_funzionamento = dati.ore_lavoro_vasche_giorno 

def collo_bottigli_pastorizzazione_giorno(numeroVasche,capacitaVasca,oreFunzionamento):
    capacità_totale = numeroVasche * capacitaVasca * oreFunzionamento
    return capacità_totale

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
flag_su_produzione_yogurt = dati.flag_pastorizzazione
if flag_su_produzione_yogurt == True:
    ########.   REPORT SEZIONE PASTORIZZAZIONE LATTE E VENDITA / ANCHE SUL CRUDO .####################
    print(f"Capacità massima di pastorizzazione:{pastorizzazione_reale_giorno_totale} litri")
    print(f"Scarto Mungitura {dati.scarto_mungitura * 100} %")
    print(f"Scarto Macchinari {dati.scarto_macchinari * 100} %")
    #Latte torico (senza scarto)
    print(f"Latte munto Atteso : {latte_giornaliero_atteso:.2f} litri")
    print(f"Latte pastorizzato effettivo : {latte_pastorizzato:.2f} litri")
    #Latte munto con lo scarto 
    print(f"Latte non pastorizzato: {latte_avanzato:.2f} litri")
    vendita_latte_crudo = latte_avanzato * dati.prezzo_latte_crudo 
    print(f"Abbiamo ricavato {vendita_latte_crudo:.2f} Euro dalla vendità del latte crudo")
    vendita_latte_pastorizzato = latte_pastorizzato * dati.prezzo_latte_pastorizzato
    print(f"Abbiamo ricavato {vendita_latte_pastorizzato:.2f} Euro dalla vendità del latte pastorizzato")
else:
    pass
###########TRASFORMAZIONE DEL LATTE PASTORIZZATO IN YOGURT #################################################
#Controllo flag di produzione yogurt
controllo_se_converto_in_yogurt = dati.flag_yogurt

def produzioneYogurt(quantoLattePastConverto,lattePastorizzato,costoAlKg,scarto):
    # 1000 litri di latte pastorizzato = 1 kg circa, per semplciità mantengo questo indice di conversione.
    # La resa reale e' gestita dal parametro "scarto" (es. 0.99).
    yogurtProdotto = quantoLattePastConverto * lattePastorizzato * scarto
    guadagnoVendita = yogurtProdotto * costoAlKg
    return yogurtProdotto, guadagnoVendita,costoAlKg,scarto

TotYogurtProdotto,TotGudaganoVenditaInKG,costoKg,scarto = produzioneYogurt(dati.percentuale_latte_dedicato_allo_yogurt,latte_pastorizzato,dati.prezzo_vendita_yogurt_fine_processo_kg,dati.percentuale_di_riuscita_resa_yogurt)
scarto_in_percentuale = scarto * 100

#LATTE PASTORIZZATO NON DESTINATO ALLO YOGURT
def lattePastorizzatoNonConvertitoInYogurt(lattePastorizzato,percentuale_latte_dedicato_allo_yogurt,prezzoVenditaLattePast):
    latte_usato_per_yogurt = percentuale_latte_dedicato_allo_yogurt * lattePastorizzato
    latte_past_rimasto_dopo_yogurt = lattePastorizzato - latte_usato_per_yogurt
    vendita_totale_latte_rimasto = latte_past_rimasto_dopo_yogurt * prezzoVenditaLattePast
    return latte_past_rimasto_dopo_yogurt,vendita_totale_latte_rimasto

latte_pastorizzato_non_destinato_allo_yogurt, vendita_latte_past_non_destinato_allo_yogurt = lattePastorizzatoNonConvertitoInYogurt(latte_pastorizzato,dati.percentuale_latte_dedicato_allo_yogurt,dati.prezzo_latte_pastorizzato)

#Produzione Yogurt + Vendità latte pastorizzato Guadagno totale
guadagno_totale_yogurt_latte_pastorizzato = TotGudaganoVenditaInKG + vendita_latte_past_non_destinato_allo_yogurt

#Blocco if che regola il report su yogurt o solo su latte pastorizzato
if controllo_se_converto_in_yogurt == True:
    print(f"Yogurt prodotto:{TotYogurtProdotto:.2f} Kg \n"f"Guadagno yogurt prodottto {TotGudaganoVenditaInKG:.2f} Euro.\n"f"E stato venduto a {costoKg} euro al KG.\nAbbiamo avuto una riuscita di {scarto_in_percentuale} %")
    print(f"Latte pastorizzato rimasto per la vendita {latte_pastorizzato_non_destinato_allo_yogurt:.2f}\n"f"Guadagno {vendita_latte_past_non_destinato_allo_yogurt:.2f} Euro.")
    print(f"Guadagno totale Latte + Yogurt {guadagno_totale_yogurt_latte_pastorizzato:.2f}")
else:
    pass

#TEST DI COERENZA SU QUANTO ALTTE UTILIZZO E QUANTO NE HO DAVVERO
latte_usato_yogurt = latte_pastorizzato * dati.percentuale_latte_dedicato_allo_yogurt

yogurt_prodotto = latte_usato_yogurt * dati.percentuale_di_riuscita_resa_yogurt

latte_rimasto = latte_pastorizzato - latte_usato_yogurt

prova = latte_usato_yogurt + latte_rimasto
print("prova",prova)
print("latte pastorizzato", latte_pastorizzato)