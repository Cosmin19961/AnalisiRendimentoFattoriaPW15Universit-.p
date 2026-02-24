#produzione yogurt a partire dal latte pastorizzato
# yogurt.py
import dati
from report import stampa_report  #hocambiato

###########TRASFORMAZIONE DEL LATTE PASTORIZZATO IN YOGURT #################################################
#Controllo flag di produzione yogurt
controllo_se_converto_in_yogurt = dati.flag_yogurt

def produzioneYogurt(quantoLattePastConverto,lattePastorizzato,costoAlKg,scarto):
    # 1000 litri di latte pastorizzato = 1 kg circa, per semplciità mantengo questo indice di conversione.
    # La resa reale e' gestita dal parametro "scarto" (es. 0.99).
    yogurtProdotto = quantoLattePastConverto * lattePastorizzato * scarto
    guadagnoVendita = yogurtProdotto * costoAlKg
    return yogurtProdotto, guadagnoVendita,costoAlKg,scarto

#LATTE PASTORIZZATO NON DESTINATO ALLO YOGURT
def lattePastorizzatoNonConvertitoInYogurt(lattePastorizzato,percentuale_latte_dedicato_allo_yogurt,prezzoVenditaLattePast):
    latte_usato_per_yogurt = percentuale_latte_dedicato_allo_yogurt * lattePastorizzato
    latte_past_rimasto_dopo_yogurt = lattePastorizzato - latte_usato_per_yogurt
    vendita_totale_latte_rimasto = latte_past_rimasto_dopo_yogurt * prezzoVenditaLattePast
    return latte_past_rimasto_dopo_yogurt,vendita_totale_latte_rimasto

def run(latte_pastorizzato):  #hocambiato
    TotYogurtProdotto,TotGudaganoVenditaInKG,costoKg,scarto = produzioneYogurt(
        dati.percentuale_latte_dedicato_allo_yogurt,
        latte_pastorizzato,
        dati.prezzo_vendita_yogurt_fine_processo_kg,
        dati.percentuale_di_riuscita_resa_yogurt
    )
    scarto_in_percentuale = scarto * 100

    latte_pastorizzato_non_destinato_allo_yogurt, vendita_latte_past_non_destinato_allo_yogurt = lattePastorizzatoNonConvertitoInYogurt(
        latte_pastorizzato,
        dati.percentuale_latte_dedicato_allo_yogurt,
        dati.prezzo_latte_pastorizzato
    )

    #Produzione Yogurt + Vendità latte pastorizzato Guadagno totale
    guadagno_totale_yogurt_latte_pastorizzato = TotGudaganoVenditaInKG + vendita_latte_past_non_destinato_allo_yogurt

    #Blocco if che regola il report su yogurt o solo su latte pastorizzato
    if controllo_se_converto_in_yogurt == True:
        stampa_report(  #hocambiato
            "report_yogurt",
            TotYogurtProdotto=TotYogurtProdotto,
            TotGudaganoVenditaInKG=TotGudaganoVenditaInKG,
            costoKg=costoKg,
            scarto_in_percentuale=scarto_in_percentuale,
        )
        stampa_report(  #hocambiato
            "report_latte_past_rimasto",
            latte_pastorizzato_non_destinato_allo_yogurt=latte_pastorizzato_non_destinato_allo_yogurt,
            vendita_latte_past_non_destinato_allo_yogurt=vendita_latte_past_non_destinato_allo_yogurt,
        )
        stampa_report(  #hocambiato
            "guadagno_totale_latte_yogurt",
            guadagno_totale_yogurt_latte_pastorizzato=guadagno_totale_yogurt_latte_pastorizzato,
        )
    else:
        pass

    #TEST DI COERENZA SU QUANTO ALTTE UTILIZZO E QUANTO NE HO DAVVERO
    latte_usato_yogurt = latte_pastorizzato * dati.percentuale_latte_dedicato_allo_yogurt
    yogurt_prodotto = latte_usato_yogurt * dati.percentuale_di_riuscita_resa_yogurt
    latte_rimasto = latte_pastorizzato - latte_usato_yogurt

#### DEBUG PRODUZIONE YOGURT ####
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