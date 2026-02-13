#VARIABILI GLOBALI
stima_su_quanti_giorni = 1
unita_di_misura = 1
mucca_lattazione = 305
mandria_A = 150 #100 mucche A produzione A
mandria_B = 100 #100 mucche B produzione B

#PREZZO VENDITA LATTE A CRUDO
prezzo_latte_crudo = 1.50 #prezzo indicativo
prezzo_latte_pastorizzato = 2.50 #prezzo indicativo

#SETTING VASCHE PASTORIZZAZIONE
numero_vasche_pastorizzazione = 10
capacita_vasca = 300 #litri
consumo_vasca_KWh = 27
ore_lavoro_vasche_giorno = 6 #ore
flag_pastorizzazione = False

scarto_mungitura = 0.02
scarto_macchinari = 0.03

costo_kwh_medio = 0.2797 #€/kWh

#DATI PRODUZIONE YOGURT
percentuale_latte_dedicato_allo_yogurt = 0.50 #decido quanto latte viene venduto pastorizzato e quanto invece viene destinato allo yogurt
flag_yogurt = True
percentuale_di_riuscita_resa_yogurt = 0.99 #tiene conto dello scarto, per ora lo metto quasi al 100%
prezzo_vendita_yogurt_fine_processo_kg = 2 * 10 # *10 in modo da avere 1000 lt == 1 kg circa di yogurt
