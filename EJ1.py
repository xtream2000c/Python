#Definir funcion que funcione como max()

n1 = input("Numero 1: ")
n2 = input("Numero 2: ")

def mayor(n1, n2):
    if n1 > n2:
        return ' es mayor que '
    else:
        return ' es menor que '

print(n1, mayor(n1, n2), n2)