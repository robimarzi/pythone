# inserire una lettere e un intero
# esempio   5  A
#         A
#        AAA
#       AAAAA


print ("dammi una lettere e un numero")
lettera = str(input())
numero = int(input())
for i in range(0, numero): 
     print (" " * (numero - i - 1) + lettera * (1+i*2))