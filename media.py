#programma per calcolare la media
contatore = int(0)   #var. contatirce per la media
numero = "0"      #conversione input in int
somma = int(0)    #somma degli input
dato = input("Inserisci i numeri da sommare per fare la media, scrivi altro per avere il risultato: ")
while dato.isdigit() :
    
    numero = int(dato)
    somma  = int(numero + somma)
    dato   = input("Prossimo numero: ")
    contatore  += 1

print("La media dei numeri scritti è", somma/contatore)


