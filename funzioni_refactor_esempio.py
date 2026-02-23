import dati

################## SEZIONE PRODUZIONE LATTE #####################################
############## ############ ############# ############### ################# ##############
# L/Anno
Bestiame = {"A": 10977, "B": 7425, "C": 7415}

# L / Giorno
Bestiame_litri_giorno = {}
for razza, litri in Bestiame.items():
    Bestiame_litri_giorno[razza] = litri / dati.mucca_lattazione


################## SEZIONE PASTORIZZAZIONE DEL LATTE #####################################
############## ############ ############# ############### ################# ##############

# Mi dice quanto latte pastorizzo considerando lo scarto di lavorazione di 5%
def Pastorizzazione(litriLatte):
    scarto = 0.05  # supponiamo che il 5% del latte lo perdiamo
    scarto_litri = litriLatte * scarto
    litri_effettivi_pastorizzati = litriLatte - scarto_litri
    return litri_effettivi_pastorizzati


# Consumo elettrico della vasca da 300 Litri
def ConsumoElettricoPastorizzazione(numero_vasche, giorni):
    consumo_kw_ore_di_lavoro = (
        dati.ore_lavoro_vasche_giorno * dati.consumo_vasca_KWh * numero_vasche * giorni
    )
    Costo_totale = consumo_kw_ore_di_lavoro * dati.costo_kwh_medio
    return giorni, dati.ore_lavoro_vasche_giorno, consumo_kw_ore_di_lavoro, Costo_totale


# LATTE PRODOTTO AL GIORNO
def prod_latte_giorno(
    latte_A, latte_B, mandria_A, mandria_B, scarto_mungitura, scarto_macchinari
):
    tot_prod_latte_giorno = (latte_A * mandria_A) + (latte_B * mandria_B)
    tot_scarto = (scarto_mungitura + scarto_macchinari) * tot_prod_latte_giorno
    tot_latte_realistico_giorno = tot_prod_latte_giorno - tot_scarto
    return tot_prod_latte_giorno, tot_latte_realistico_giorno


# CAPACITA MASSIMA DI PASTORIZZAZIONE
def collo_bottigli_pastorizzazione_giorno(numeroVasche, capacitaVasca, oreFunzionamento):
    capacità_totale = numeroVasche * capacitaVasca * oreFunzionamento
    return capacità_totale


########### TRASFORMAZIONE DEL LATTE PASTORIZZATO IN YOGURT #################################################
def produzioneYogurt(quantoLattePastConverto, lattePastorizzato, costoAlKg, scarto):
    # 1000 litri di latte pastorizzato = 1 kg circa, per semplciità mantengo questo indice di conversione.
    # La resa reale e' gestita dal parametro "scarto" (es. 0.99).
    yogurtProdotto = quantoLattePastConverto * lattePastorizzato * scarto
    guadagnoVendita = yogurtProdotto * costoAlKg
    return yogurtProdotto, guadagnoVendita, costoAlKg, scarto


# LATTE PASTORIZZATO NON DESTINATO ALLO YOGURT
def lattePastorizzatoNonConvertitoInYogurt(
    lattePastorizzato, percentuale_latte_dedicato_allo_yogurt, prezzoVenditaLattePast
):
    latte_usato_per_yogurt = percentuale_latte_dedicato_allo_yogurt * lattePastorizzato
    latte_past_rimasto_dopo_yogurt = lattePastorizzato - latte_usato_per_yogurt
    vendita_totale_latte_rimasto = latte_past_rimasto_dopo_yogurt * prezzoVenditaLattePast
    return latte_past_rimasto_dopo_yogurt, vendita_totale_latte_rimasto

def esegui_report():  # CAMBIO
    latte_A = Bestiame_litri_giorno["A"]
    latte_B = Bestiame_litri_giorno["B"]
    mandria_A = dati.mandria_A
    mandria_B = dati.mandria_B
    scarto_mungitura = dati.scarto_mungitura
    scarto_macchinari = dati.scarto_macchinari

    numero_vasche = dati.numero_vasche_pastorizzazione
    capacità_vasca = dati.capacita_vasca
    ore_funzionamento = dati.ore_lavoro_vasche_giorno

    pastorizzazione_reale_giorno_totale = collo_bottigli_pastorizzazione_giorno(
        numero_vasche, capacità_vasca, ore_funzionamento
    )

    # ECCESSO DI PRODUZZIONE vs CAPACITà DI PASTORIZZAZIONE
    latte_giornaliero_atteso, latte_giornalieto_munto = prod_latte_giorno(
        latte_A, latte_B, mandria_A, mandria_B, scarto_mungitura, scarto_macchinari
    )
    capacita_massima_past_giorno = collo_bottigli_pastorizzazione_giorno(
        numero_vasche, capacità_vasca, ore_funzionamento
    )  # qui metto la capacità massima di pastorizzazione

    latte_avanzato = 0
    latte_pastorizzato = 0
    if latte_giornalieto_munto > capacita_massima_past_giorno:
        latte_avanzato = latte_giornalieto_munto - capacita_massima_past_giorno
        latte_pastorizzato = capacita_massima_past_giorno
    else:
        latte_pastorizzato = latte_giornalieto_munto

    # Se vendo yogurt, allora devo considerare i litri di latte totali che destinerò allo yogurt e venderò la rimanenza
    # Blocco da finire
    flag_su_produzione_yogurt = dati.flag_pastorizzazione
    if flag_su_produzione_yogurt is True:
        ########.   REPORT SEZIONE PASTORIZZAZIONE LATTE E VENDITA / ANCHE SUL CRUDO .####################
        _stampa(  # CAMBIO
            "capacita_massima_pastorizzazione",
            pastorizzazione_reale_giorno_totale=pastorizzazione_reale_giorno_totale,
        )
        _stampa("scarto_mungitura", scarto_mungitura_percent=dati.scarto_mungitura * 100)  # CAMBIO
        _stampa("scarto_macchinari", scarto_macchinari_percent=dati.scarto_macchinari * 100)  # CAMBIO
        # Latte torico (senza scarto)
        _stampa("latte_munto_atteso", latte_giornaliero_atteso=latte_giornaliero_atteso)  # CAMBIO
        _stampa("latte_pastorizzato_effettivo", latte_pastorizzato=latte_pastorizzato)  # CAMBIO
        # Latte munto con lo scarto
        _stampa("latte_non_pastorizzato", latte_avanzato=latte_avanzato)  # CAMBIO
        vendita_latte_crudo = latte_avanzato * dati.prezzo_latte_crudo
        _stampa("ricavo_latte_crudo", vendita_latte_crudo=vendita_latte_crudo)  # CAMBIO
        vendita_latte_pastorizzato = latte_pastorizzato * dati.prezzo_latte_pastorizzato
        _stampa(  # CAMBIO
            "ricavo_latte_pastorizzato",
            vendita_latte_pastorizzato=vendita_latte_pastorizzato,
        )
    else:
        pass

    # Controllo flag di produzione yogurt
    controllo_se_converto_in_yogurt = dati.flag_yogurt
    TotYogurtProdotto, TotGudaganoVenditaInKG, costoKg, scarto = produzioneYogurt(
        dati.percentuale_latte_dedicato_allo_yogurt,
        latte_pastorizzato,
        dati.prezzo_vendita_yogurt_fine_processo_kg,
        dati.percentuale_di_riuscita_resa_yogurt,
    )
    scarto_in_percentuale = scarto * 100

    (
        latte_pastorizzato_non_destinato_allo_yogurt,
        vendita_latte_past_non_destinato_allo_yogurt,
    ) = lattePastorizzatoNonConvertitoInYogurt(
        latte_pastorizzato,
        dati.percentuale_latte_dedicato_allo_yogurt,
        dati.prezzo_latte_pastorizzato,
    )

    # Produzione Yogurt + Vendità latte pastorizzato Guadagno totale
    guadagno_totale_yogurt_latte_pastorizzato = (
        TotGudaganoVenditaInKG + vendita_latte_past_non_destinato_allo_yogurt
    )

    # Blocco if che regola il report su yogurt o solo su latte pastorizzato
    if controllo_se_converto_in_yogurt is True:
        _stampa(  # CAMBIO
            "report_yogurt",
            TotYogurtProdotto=TotYogurtProdotto,
            TotGudaganoVenditaInKG=TotGudaganoVenditaInKG,
            costoKg=costoKg,
            scarto_in_percentuale=scarto_in_percentuale,
        )
        _stampa(  # CAMBIO
            "report_latte_past_rimasto",
            latte_pastorizzato_non_destinato_allo_yogurt=latte_pastorizzato_non_destinato_allo_yogurt,
            vendita_latte_past_non_destinato_allo_yogurt=vendita_latte_past_non_destinato_allo_yogurt,
        )
        _stampa(  # CAMBIO
            "guadagno_totale_latte_yogurt",
            guadagno_totale_yogurt_latte_pastorizzato=guadagno_totale_yogurt_latte_pastorizzato,
        )
    else:
        pass

    # TEST DI COERENZA SU QUANTO ALTTE UTILIZZO E QUANTO NE HO DAVVERO
    latte_usato_yogurt = latte_pastorizzato * dati.percentuale_latte_dedicato_allo_yogurt

    yogurt_prodotto = latte_usato_yogurt * dati.percentuale_di_riuscita_resa_yogurt

    latte_rimasto = latte_pastorizzato - latte_usato_yogurt

    prova = latte_usato_yogurt + latte_rimasto
    _stampa("prova", prova=prova)  # CAMBIO
    _stampa("latte_pastorizzato", latte_pastorizzato=latte_pastorizzato)  # CAMBIO

#Questa funzione serve per richiamare il report di stampa.
#Cosa fa esattamente ?
#Riceve una chiave in ingresso (esempio ltte_munto_atteso) 
#prende il messaggio di stampa contenuto nel report con la relativa chiave e stampa i parametri 
#Perchè utilizzo kwargs?
#Per via dell'utilizzo del report nel dizionario, se lo richiamassi senza kwargs mi tornerebbe una stringa e non il valore effettivo calcolato dalla funzione che ho richiesto.
#kwargs -> raccoglie il valore
#.format(**kwargs) lo inserisce nel testo 
def _stampa(chiave, **kwargs):  # CAMBIO
    print(MESSAGGI_STAMPA[chiave].format(**kwargs))  # CAMBIO

MESSAGGI_STAMPA = {  # CAMBIO
    "capacita_massima_pastorizzazione": "Capacità massima di pastorizzazione:{pastorizzazione_reale_giorno_totale} litri",  # CAMBIO
    "scarto_mungitura": "Scarto Mungitura {scarto_mungitura_percent} %",  # CAMBIO
    "scarto_macchinari": "Scarto Macchinari {scarto_macchinari_percent} %",  # CAMBIO
    "latte_munto_atteso": "Latte munto Atteso : {latte_giornaliero_atteso:.2f} litri",  # CAMBIO
    "latte_pastorizzato_effettivo": "Latte pastorizzato effettivo : {latte_pastorizzato:.2f} litri",  # CAMBIO
    "latte_non_pastorizzato": "Latte non pastorizzato: {latte_avanzato:.2f} litri",  # CAMBIO
    "ricavo_latte_crudo": "Abbiamo ricavato {vendita_latte_crudo:.2f} Euro dalla vendità del latte crudo",  # CAMBIO
    "ricavo_latte_pastorizzato": "Abbiamo ricavato {vendita_latte_pastorizzato:.2f} Euro dalla vendità del latte pastorizzato",  # CAMBIO
    "report_yogurt": "Yogurt prodotto:{TotYogurtProdotto:.2f} Kg \nGuadagno yogurt prodottto {TotGudaganoVenditaInKG:.2f} Euro.\nE stato venduto a {costoKg} euro al KG.\nAbbiamo avuto una riuscita di {scarto_in_percentuale} %",  # CAMBIO
    "report_latte_past_rimasto": "Latte pastorizzato rimasto per la vendita {latte_pastorizzato_non_destinato_allo_yogurt:.2f}\nGuadagno {vendita_latte_past_non_destinato_allo_yogurt:.2f} Euro.",  # CAMBIO
    "guadagno_totale_latte_yogurt": "Guadagno totale Latte + Yogurt {guadagno_totale_yogurt_latte_pastorizzato:.2f}",  # CAMBIO
    "prova": "prova {prova}",  # CAMBIO
    "latte_pastorizzato": "latte pastorizzato {latte_pastorizzato}",  # CAMBIO
}


if __name__ == "__main__":  # CAMBIO
    esegui_report()  # CAMBIO
