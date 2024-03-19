#Neo Armada

#Programa que pida números hasta que se inserte un 0. 
#Posteriormente, el programa visualizará el resultado de 
#multiplicar todos los números insertados (excepto el 0). 
#Si introduce un 0 como primer número debe mostrar por 
#pantalla un mensaje indicando que no podemos hacer el
#producto y terminar el programa.

acumulador=1
opcion=1

while opcion != 0:
    acumulador*=opcion
    opcion=int(input("Dame un numero: "))

print(acumulador)