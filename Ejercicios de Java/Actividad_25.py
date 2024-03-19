#Neo Armada

#Programa que pida varios números hasta que el usuario 
#inserte un número par. Hay que ir visualizando cada uno 
#de los números insertados (excepto el número par). Cuando 
#termine porque ha insertado un número para debe mostrar un 
#mensaje indicándolo.

numero=int(input("Dame un numero: "))
while numero%2 != 0:
    print(numero)
    numero=int(input("Dame un numero: "))