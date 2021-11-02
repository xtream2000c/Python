#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

lista = [0] * 4
lista[0] = input("Primer numero de la lista: ")
lista[1] = input("Segundo numero de la lista: ")
lista[2] = input("Tercero numero de la lista: ")
lista[3] = input("Cuarto numero de la lista: ")

print(lista)
def suma(lista):
    suma = 0
    for objeto in lista:
        suma += int(objeto)
    return suma

def multiplicacion(lista):
    multiplicacion = 1
    for objeto in lista:
        multiplicacion *= int(objeto)
    return multiplicacion

print("La suma de: ", lista, " es: ", suma(lista))
print("La multiplicacion de: ", lista, " es: ", multiplicacion(lista))