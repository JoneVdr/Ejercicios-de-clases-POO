"""Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

a = A
y = a.z
print(y(a))
aa = a()
print(aa is a())
z = aa.y
print(z(()))
print(a().y((a,)))
print(A.y(aa, (a,z)))
print(aa.y((z,1,'z'))) """
class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

a = A
y = a.z
print(y(a))
aa = a()
print(aa is a())
z = aa.y
print(z(()))
print(a().y((a,)))
print(A.y(aa, (a,z)))
print(aa.y((z,1,'z')))

""" class A:
    def z(self):
        return self

    def y(self, t):
        return len(t) =

Lo primero que hace el código es definir una clase A con dos métodos que son z e y. El método z devuelve la instancia actual que es self, el método y, en cambio toma un argumento t y devuelve la longitud de ese argumento t.

a = A = Se crea una variable a que se refiere a la clase A.
y = a.z
print(y(a)) = Se crea una variable y que se refiere al método z de la clase A. Se llama al método z en a y se pasa a como argumento. Por lo que esto devuelve la clase A.

aa = a()
print(aa is a()) = Despues de esto se crea una instancia de la clase A llamada aa. Se comprueba que aa es igual a otra instancia creada de la clase A. Esto devuelve False porque son instancias diferentes.

z = aa.y
print(z(())) = A continuacion, se crea una variable z que se refiere al método y de la instancia aa. Se llama al metodo y en aa y se pasa una tupla vacia como argumento. Esta parte devuelve 0, porque la longitud de una tupla vacia es 0.

print(A.y(aa, (a,z))) = Se llama al metodo y en la nueva instancia de la clase A, y se le pasa una tupla que ocntiene la clase A y la variable z. Esto devuelve 2, porque la longitud de la tupla es 2.

print(aa.y((z,1,'z'))) = Por último, se llama al metodo y en la instancia aa y se le pasa una tupla que contiene la variable z, en entero 1 y la cadena z. Esto devuelve un error tipo TypeError, porque el método y espera una tupla de objetos que se pueden calcular con longitud, y el entero y la cadena no son objetos que puedan tener una longitud"""