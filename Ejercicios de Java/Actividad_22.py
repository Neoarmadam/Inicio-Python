#Neo Armada

#Programa que pida dos números enteros. Posteriormente, 
#el usuario deberá indicar la operación que quiere
#realizar sobre esos datos. Para ello, indicará:
#➢ Un * si quiere multiplicarlos. (Si 
#te ves mal haz esto si pulsa 1)
#➢ Un + si quiere sumarlos. 
#(Si te ves mal haz esto si pulsa 2)
#➢ Un - si quiere restarlos. (Si te ves mal haz esto si pulsa 3)
#➢ Un % o / si quiere visualizar el cociente y el 
#resto de una división entera. Visualizará estos dos resultados
#(independientemente que indique / o %). 
#(Si te ves mal haz esto si pulsa 4 o 5)
#Si el usuario no indicara ninguno de estos caracteres, 
#se visualizará un mensaje de error.

print("Te voy a pedir dos numeros, y que hacer con ellos")

num1=int(input("Dame el primer numero: "))
num2=int(input("Dame el segundo numero: "))

print("*: Multiplicar")
print("+: Sumar")
print("-: Restar")
print("/: Dividir")

opcion=input("Eliga una opcion: ")

if opcion == "*" or opcion == "1":
    print("El resultado es "+str(num1*num2))
elif opcion =="+" or opcion=="2":
    print("El resultado es "+str(num1+num2))
elif opcion=="-" or opcion=="3":
    print("El resultado es "+str(num1-num2))
elif opcion=="/" or opcion=="4":
    print("El resultado es "+str(num1/num2)+" y el resto "+str(num1%num2))
else:
    print("opcion no valida")