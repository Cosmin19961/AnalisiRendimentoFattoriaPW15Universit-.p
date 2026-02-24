#RUN -> da qui parte l'esecuzione del programma

# main.py
import latte_pastorizzato as latte_mod  #hocambiato
import yogurt  # ok

def main():
    latte_pastorizzato = latte_mod.run()  #hocambiato
    yogurt.run(latte_pastorizzato)

if __name__ == "__main__":
    main()