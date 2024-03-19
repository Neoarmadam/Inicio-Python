#Neo Armada

#Programa que lea un número y debe mostrar por pantalla 
#si es positivo,negativo o cero.

numero = int(input("Dame un numero: " )) #Hay que especificar que es int para la comparacion.

if numero < 0:
    print("El numero introducido es negativo")
else:
    print("El numero introducido es positivo")