#Neo Armada

#Programa que pida al usuario un número del 1 al 7 y 
#visualice el nombre del día en función de dicho valor.
#Si el número que introduce el usuario no es del 1 al 7 
#finaliza el programa con un mensaje explicativo.

#Funcion que hace de Switch
def swicht(arg):
    switcher= {
        1:"Lunes",
        2:"Martes",
        3:"Miercoles",
        4:"Jueves",
        5:"Viernes",
        6:"Sabado",
        7:"Domingo"
    }
    return switcher.get(arg, "Opcion no valida")

opcion= int(input("Dame un numero del 1-7: "))
print(swicht(opcion))