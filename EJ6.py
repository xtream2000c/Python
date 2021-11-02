#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

año = input("Año en curso: ")
personas =['none'] * 3

personas[0] = input("Nombre: "), input("año nacimiento: ")
personas[1] = input("Nombre: "), input("año nacimiento: ")
personas[2] = input("Nombre: "), input("año nacimiento: ")

edades=['none'] * 3
contador = 0

for persona in personas:
    edades[contador] = persona[0], int(año) - int(persona[1])
    contador +=1

for edad in edades:
    print(edad)