#RUN -> da qui parte l'esecuzione del programma

# main.py
import latte_pastorizzato as latte_mod  #hocambiato
import yogurt  # ok

#Questa def principale gestisce l'ordine di attivazione dei file
#Senza rischio di richiamare delle funzioni che ancora non hanno il valore 

def main():
    latte_pastorizzato = latte_mod.run()  #hocambiato
    yogurt.run(latte_pastorizzato)

if __name__ == "__main__":
    main()