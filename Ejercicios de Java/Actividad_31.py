#Neo Armada

#Escribe un programa que pida tantos números como el usuario
#le indique al principio. El programa debe visualizar, al 
#final del programa, la media de todos los números insertados 
#y si se ha insertado algún par.

repeticion=int(input("Dame cuantos numeros me vas a dar: "))
pares=0
acumulador=0
for f in range(repeticion):
    numero=int(input("Dame el numero "+str(f+1)+"º: "))
    acumulador+=numero
    if numero%2==0:
        pares+=1
    
print("La media es de "+str(acumulador/repeticion)+" y has introducido "+str(pares)+" numeros pares.")