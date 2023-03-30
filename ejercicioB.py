"""Enunciado: en esta misma clase Palindromo, añada un atributo que se inicializará en el constructor. Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia, muestre el atributo en mayúsculas.

Comportamiento esperado:

p = Palindromo("radar")
print(p.test())
>>> True
p = Palindromo("sonar")
>>> RADAR
print(p.test())
>>> False
SONAR
Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")? """
from ejercicioA import Palindromo
class Palindromo(Palindromo):
    def __init__(self, palabra):
        super().__init__(palabra)
    def test(self):
        if self.esPalindromo(self.palabra):
            return True
        else:
            return False
    def __del__(self): #Destructor
        print(self.palabra.upper())


p = Palindromo("radar")
print(p.test())
p = Palindromo("sonar")
print(p.test())


'''
Despues de la instanción Palindromo ("sonar") se muestra RADAR porque el método destructor
imprime la palabra en mayúsculas, y la palabra es "radar" porque es la última palabra que se
instanció. Al ejecutar p = Palindromo("radar") se ejecuta del"'''
