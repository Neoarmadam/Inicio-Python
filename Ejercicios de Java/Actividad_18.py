#Neo Armada

#Programa que lea tres números y visualice el más pequeño de los tres.

print("Te voy a pedir tres numeros")

num1=int(input("Dame el primer numero: "))
num2=int(input("Dame el segundo numero: "))
num3=int(input("Dame el tercer numero: "))

if num1>num2 & num1>num3:
    print("El numero "+str(num1)+" es el mayor") #Necesario pasar el int a string para concatenar
elif num2>num1 & num2>num3:
    print("El numero "+str(num2)+" es el mayor")
else:
    print("El numero "+str(num3)+" es el mayor")

print("Gracias por jugar")