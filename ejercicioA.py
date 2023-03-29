"""Enunciado: crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

Comportamiento esperado:

print(Palindromo.esPalindromo('radar'))
>>> True
print(Palindromo.esPalindromo('sonar'))
>>> False
print(Palindromo.esPalindromo('Arde ya la yedra'))
>>> False
print(Palindromo.esPalindromo('Ardeyalayedra'))
>>> True
print(Palindromo.esPalindromo('!@#$% %$#@!'))
>>> True
print(Palindromo.esPalindromo('L O L'))
>>> True """


class Palindromo:
    def __init__(self, palabra):
        self.palabra = str(palabra)

    @classmethod #Decorador classmethod porque no usa ninguna propiedad de instancia de Palindromo, sino que solo se basa en el argumento que se pasa como entrada.
    def esPalindromo(cls, palabra):
        palabra = palabra.lower()
        if palabra == palabra[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Palindromo.esPalindromo('radar'))
    print(Palindromo.esPalindromo('sonar'))
    print(Palindromo.esPalindromo('Arde ya la yedra'))
    print(Palindromo.esPalindromo('Ardeyalayedra'))
    print(Palindromo.esPalindromo('!@#$% %$#@!'))
    print(Palindromo.esPalindromo('L O L'))


'''
DEVUELVE:
>>> True
>>> False
>>> False
>>> True
>>> True
>>> True
'''
