"""Enunciado: Escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada() de una clase Test.

Comportamiento esperado:

test = Test()
for i in range(1, 6):
   if i == 1:
       test.llamada("Primera llamada")
   else:
       test.llamada("{}ª llamada".format(string))
$> cat log.txt
--Start log--
Primera llamada
2a llamada
3a llamada
4a llamada
5a llamada
--End log: 5 log(s)--
"""
class Logger:
    def __init__(self, archivo):
        self.archivo = archivo
        self.contador = 0
        with open(self.archivo, "w") as log:
            log.write("--Start log--\n")
    def log(self, mensaje):
        with open(self.archivo, "a") as log:
            log.write(mensaje + "\n")
            self.contador += 1
    def __del__(self):
        with open(self.archivo, "a") as log:
            log.write("--End log: {} log(s)--".format(self.contador))


class Test(Logger):
    def __init__(self):
        super().__init__("log.txt")

    def llamada(self, mensaje):
        self.log(mensaje)

test = Test()
for i in range(1, 6):
   if i == 1:
       test.llamada("Primera llamada")
   else:
       test.llamada("{}ª llamada".format(i))
