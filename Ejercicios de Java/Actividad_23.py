#Neo Armada

#Programa que pida al usuario 10 números y salga por pantalla la media de ellos.

acumulador=0
repeticiones=10

for f in range(repeticiones):
    entrada=int(input("Dame el numero "+str(f+1)+"º: "))
    acumulador+=entrada
print("La media es de "+str(acumulador/repeticiones))