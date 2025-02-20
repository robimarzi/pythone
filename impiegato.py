class Employee :
    def __init__(self, nome, cognome, salario):
        self._salario = salario
        self._nome = nome
        self._cognome = cognome


    
class Manager (Employee) :
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario)
        self._reparto = reparto

    def __repr__(self):

        return self._nome + " " + self._cognome + " " + self._salario + " " + self._reparto 
    
x = Manager ("Marco", "rossi", "1500", "capo")


print(x)

