#Neo Armada

#Programa que lea una serie de números hasta que se introduzca
#un cero. El programa debe visualizar, al final del programa, 
#la suma de todos los números positivos insertados y la cantidad 
#de números (en total) que se han insertado(incluido el cero).

numero= -1
contador=0
acumulador=0

while numero != 0:
    numero=int(input("Dame un numero: "))
    if numero >= 0:
        contador+=1
        acumulador+=numero

print("Suma: "+str(acumulador))
print("Numero de positivos: "+str(contador))