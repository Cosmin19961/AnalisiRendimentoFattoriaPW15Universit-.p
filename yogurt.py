#produzione yogurt a partire dal latte pastorizzato
# yogurt.py
import dati
from report import stampa_report  #hocambiato

###########TRASFORMAZIONE DEL LATTE PASTORIZZATO IN YOGURT #################################################
#Controllo flag di produzione yogurt / Se questo flag è su True, allora vuol dire che la produzione di yogurt è attiva e quindi genera il report.
controllo_se_converto_in_yogurt = dati.flag_yogurt

def produzioneYogurt(quantoLattePastConverto,lattePastorizzato,costoAlKg,scarto):
    # 1000 litri di latte pastorizzato = 1 kg circa, per semplciità mantengo questo indice di conversione.
    # La resa reale e' gestita dal parametro "scarto" (es. 0.99).
    #Qui calcolo quanto yogurt produco
    #Mi serve sapere quanto latte pastorizzato convergo verso lo yogurt
    #Moltiplico quella % per il latte pastorizzato e per lo scarto ( ottenendo lo yogurt reale prodotto )
    yogurtProdotto = quantoLattePastConverto * lattePastorizzato * scarto 
    #Qui semplicemente il quantitativo di yogurt prodotto e lo moltiplico per il costo al KG ottenendo la resa economica
    guadagnoVendita = yogurtProdotto * costoAlKg
    #Come ritorno della funzione ho : Lo yogurt totale prodotto / il guadagno della vendita / il costo al KG al quale ho venduto / Scarto considerato
    #Dove prendo i valori da passare alla funzione?
    return yogurtProdotto, guadagnoVendita,costoAlKg,scarto

#LATTE PASTORIZZATO NON DESTINATO ALLO YOGURT
def lattePastorizzatoNonConvertitoInYogurt(lattePastorizzato,percentuale_latte_dedicato_allo_yogurt,prezzoVenditaLattePast):
    latte_usato_per_yogurt = percentuale_latte_dedicato_allo_yogurt * lattePastorizzato
    latte_past_rimasto_dopo_yogurt = lattePastorizzato - latte_usato_per_yogurt
    vendita_totale_latte_rimasto = latte_past_rimasto_dopo_yogurt * prezzoVenditaLattePast
    return latte_past_rimasto_dopo_yogurt,vendita_totale_latte_rimasto
    #Mi torna : dopo la conversione in yogurt, quanto latte past mi è rimasto. Vendita di questo latte rimasto pastorizzato e non impiegato per lo yogurt.

#Questa funzione richiama la produzione di yogurt passandogli i valori necessari per il funzionamento
def run(latte_pastorizzato): 
    TotYogurtProdotto,TotGudaganoVenditaInKG,costoKg,scarto = produzioneYogurt(
        dati.percentuale_latte_dedicato_allo_yogurt, #Prendo la % di latte destinato da dati
        latte_pastorizzato, #Gli passo il quantitativo di latte pastorizzato totale ottenuto con la pastorizzazione del latte 
        dati.prezzo_vendita_yogurt_fine_processo_kg, #Prende il prezzo che ho definito in dati per la vendita dello yogurt
        dati.percentuale_di_riuscita_resa_yogurt #Prende lo scarto in considerazione, o meglio 
    )
    scarto_in_percentuale = scarto * 100 #Converto lo scarto in %

    #Mi torna : dopo la conversione in yogurt, quanto latte past mi è rimasto. Vendita di questo latte rimasto pastorizzato e non impiegato per lo yogurt.
    latte_pastorizzato_non_destinato_allo_yogurt, vendita_latte_past_non_destinato_allo_yogurt = lattePastorizzatoNonConvertitoInYogurt(
        latte_pastorizzato, #Passo il latte pastorizzato totale
        dati.percentuale_latte_dedicato_allo_yogurt, #Passo % di latte da convertire in yogurt
        dati.prezzo_latte_pastorizzato #Passo i dati del prezzo a cui vendo il latte pastorizzato
    )

    #Produzione Yogurt + Vendità latte pastorizzato Guadagno totale
    #Qui calcolo quanto guadagno in totale dalla vendita dello yogurt e del latte pastorizzato non convertito in yogurt
    guadagno_totale_yogurt_latte_pastorizzato = TotGudaganoVenditaInKG + vendita_latte_past_non_destinato_allo_yogurt

    #Blocco if che regola il report su yogurt o solo su latte pastorizzato
    #Se il flag è ATTIVO allora genero il reporto della conversione in yogurt, altrimenti no.
    if controllo_se_converto_in_yogurt == True:
        stampa_report( 
            "report_yogurt",
            TotYogurtProdotto=TotYogurtProdotto,
            TotGudaganoVenditaInKG=TotGudaganoVenditaInKG,
            costoKg=costoKg,
            scarto_in_percentuale=scarto_in_percentuale,
        )
        stampa_report(
            "report_latte_past_rimasto",
            latte_pastorizzato_non_destinato_allo_yogurt=latte_pastorizzato_non_destinato_allo_yogurt,
            vendita_latte_past_non_destinato_allo_yogurt=vendita_latte_past_non_destinato_allo_yogurt,
        )
        stampa_report( 
            "guadagno_totale_latte_yogurt",
            guadagno_totale_yogurt_latte_pastorizzato=guadagno_totale_yogurt_latte_pastorizzato,
        )
    else:
        pass

    #TEST DI COERENZA SU QUANTO ALTTE UTILIZZO E QUANTO NE HO DAVVERO
    latte_usato_yogurt = latte_pastorizzato * dati.percentuale_latte_dedicato_allo_yogurt
    yogurt_prodotto = latte_usato_yogurt * dati.percentuale_di_riuscita_resa_yogurt
    latte_rimasto = latte_pastorizzato - latte_usato_yogurt

#### DEBUG PRODUZIONE YOGURT #### 24/02
#### Se dopo la conversione del latte pastorizzato in yogurt ho un'incongruenza tra il totale latte utilizzato e rimanenza eventuale. 
#### Sul totale prodotto, mi genera un errore. Serve ad evitare di aver trasformato più latte di quello effettivamente prodotto in totale.
    if dati.debug_coerenza_totale_latte == True:
        coerenza_totale_latte_dopo_produzione_yogurt = latte_usato_yogurt + latte_rimasto
        if coerenza_totale_latte_dopo_produzione_yogurt == latte_pastorizzato:
            print("Hai coerenza nei dati tra yogurt / latte rimanente e totale latte pastorizzato prod")
        else:    
            print("coerenza_totale_latte_dopo_produzione_yogurt",coerenza_totale_latte_dopo_produzione_yogurt)
            print(f"Totale latte pastorizzato usato per lo yogurt + latte rimasto pastorizzato {coerenza_totale_latte_dopo_produzione_yogurt:.0f}")
            print(f"Latte pastorizzato totale {latte_pastorizzato:.0f}")

    return True  #hocambiato (solo per dire "finito", se non ti serve lo togliamo)