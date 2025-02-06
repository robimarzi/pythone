# esempio_01.py
# inserire dei numeri float e fermare il conteggio quando le ultime due letture sono uguali  0
i = 0.00    
somma = 0    # var somma
conta = 0
print("Inserisci dei numeri, di cui fare la somma")

while True :
    i = float(input())
    somma += i
    if i == 0 :
        conta += 1
        if conta == 2 :
            print ("La somma è:", somma)
            break
    else :
        conta = 0
    