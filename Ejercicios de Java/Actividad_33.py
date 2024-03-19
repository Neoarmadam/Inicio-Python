#Neo Armada

#Modifica el programa anterior, de tal forma que el programa no 
#pida 10 notas, sino que vaya pidiendo notas hasta que el 
#usuario inserte una nota incorrecta, es decir, una nota 
#que no esté entre 0 y 10.

aprobados=0
numero=0
while numero>=0 and numero<=10:
    numero=int(input("Dame la nota del alumno: "))
    if numero>5:
        aprobados+=1

print("Han aprobado "+str(aprobados)+" alumnos")