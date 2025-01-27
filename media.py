#programma per calcolare la media
count = int(0)   #var. contatirce per la media
numero = "0"     #input utente 
somma = int(0)   #somma degli in put
dato = input("Inserisci i numeri da sommare per fare la media, scrivi altro per avere la media: ")
while dato.isdigit() :
    
    numero = int(dato)
    somma  = int(numero + somma)
    dato   = input()
    count  = count + 1

print("La media dei numeri scritti è", somma/count )


