# # variable controladora

# numero = 1

# # declaro el ciclo
# while(numero <= 20):
#     print("Samantha mi reina")
#     print(numero)
#     numero+=1

# importar librerias 
import math



print("Empanadas el machetico")
print("**********************")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un #")
print("2. Digita 2 para calcular la potencia 2 de un #")
print("**********************")

opcion = 1


while(opcion != 0):
    opcion = int(input("Digita una opcion: "))

    if(opcion == 0):
        break
    elif(opcion == 1):
        numero = int(input("Digita un numero: "))
        raiz = math.sqrt(numero)
        print(f"La raiz cuadrada de {numero} es: {raiz} ")
    elif(opcion == 2):
        numero = int(input("Digita un numero: "))
        potencia = math.pow(numero, 2)
        print(f"La potencia de {numero} es: {potencia} ")

    else:
        print("Opción no disponible")

