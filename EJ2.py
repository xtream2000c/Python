#Definir funcion que funcione como max() pero 3 numeros

n1 = input("Numero 1: ")
n2 = input("Numero 2: ")
n3 = input("Numero 3: ")

def mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3 :
        return n1
    elif n2 >= n1 and n2 >= n3 :
        return n2
    else:
        return n3

print("El numero mayor es: ",mayor(n1, n2, n3))