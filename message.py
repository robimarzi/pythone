class Message :
    def __init__(self, mittente, destinatario):
        self._mittente = mittente
        self._destinatario = destinatario
        self._corpoMessaggio = []

    def append (self, rigaTesto) :
        self._corpoMessaggio.append(rigaTesto)
    
    def toString (self) :
        x = ' '.join(self._corpoMessaggio)
        print (self._mittente, "scrive a", self._destinatario, x)
    
    
noStampa = True
x = input ("Dammi il mittente del messaggio ")
y = input ("Dammi il destinatario ") 
email = Message (x, y)
while noStampa : 
    msg = input("Dimmi il messaggio:")
    email.append(msg)
    print ("Premi invio se vuoi stampare il messaggio, digita qualsiasi cosa per stampare il messaggio")
    x = ""
    x = input()
    if x == "" : 
        noStampa = False

email.toString()


        