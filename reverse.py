
import os 
nomeFile = input("Dammi il nome del file da aprire: ")
if os.path.exists(nomeFile):   
    with open (nomeFile, "r") as fh:
        lista = fh.readlines()
        for riga in lista :
            a = list(riga)
            a.reverse()
            print("".join(a))
else:
    print(f"Non trovato il file '{nomeFile}'")

