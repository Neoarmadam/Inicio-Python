#Neo Armada

#Escribir un programa que calcule la suma de 6 números que
#inserte el usuario a través del teclado

acumulador=0
for f in range(6):
    numero=int(input("Dame el "+str(f+1)+"º numero: "))
    acumulador+=numero
print("La suma es :"+str(acumulador))