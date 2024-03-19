#Neo Armada

#Programa que inserte cada una de las notas que han obtenido 10
#alumnos en el módulo de programación. Hay que validar que las 
#notas insertadas estén entre 0 y 10. Si no es así, se volverá 
#a pedir la nota. Al final de programa, hay que visualizar 
#cuántos alumnos han aprobado el módulo.

aprobados=0

for f in range(10):
    numero=int(input("Dame la nota del alumno: "))
    while numero<0 or numero>10:
        numero=int(input("Nota no valida: "))
    if numero>5:
        aprobados+=1

print("Han aprobado "+str(aprobados)+" alumnos")