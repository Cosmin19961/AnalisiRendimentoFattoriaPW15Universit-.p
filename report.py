#sezione report, tutte le stampe partono da qui# report.py
################################# CONTENITORE STAMPE #############################################################

def stampa_report(nome_variabile_da_ricercare, **kwargs):  # CAMBIO changereport
    print(Contenitore_Stampa_Report[nome_variabile_da_ricercare].format(**kwargs))  # CAMBIO changereport

Contenitore_Stampa_Report = {  # CAMBIO
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
    "coerenza_latte_su_yogurt": "Totale latte impiegato tra yogurt e rimanenza pastorizzata {coerenza_latte_su_yogurt:.0f}",  # CAMBIO changereport
    "latte_pastorizzato": "latte pastorizzato {latte_pastorizzato:.0f}",  # CAMBIO changereport
}
