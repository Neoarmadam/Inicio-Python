#Neo Armada

#programa que pida un número del 1 al 7 asociado 
#a un día de la semana y visualizar si es laborable o
#festivo

#Funcion que hace de Switch
def swicht(arg):
    switcher= {
        1|2|3|4|5:"Laborable",
        6|7:"No Laborable"
    }
    return switcher.get(arg, "Opcion no valida")

opcion= int(input("Dame un numero del 1-7: "))
print(swicht(opcion))