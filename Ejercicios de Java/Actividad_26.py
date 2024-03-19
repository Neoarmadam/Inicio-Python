#Neo Armada

#Programa que pida al usuario números hasta que el número
#insertado sea mayor o igual que 10. Cuando inserte 
#un número mayor que 10 termina el programa con un mensaje 
#que lo indique e imprimiendo el número.

numero=0

while numero < 10:
    numero=int(input("Dame un numero: "))

if numero != 10:
    print(numero)