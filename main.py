# ejemplo de estaciones

mes = input("Digita un mes del año por favor: ").lower()
if (mes == "diciembre" or mes == "enero" or mes == "febrero" or mes == "marzo" ):
    print(f"el mes {mes} pertenece a invierno")
elif(mes == "junio" or mes == "julio" or mes == "agosto"):
    print(f"el mes {mes} pertenece a verano")
elif(mes == "abril" or mes == "mayo"):
    print(f"el mes {mes} pertenece a primavera")
else:
    print(f"el mes {mes} pertenece a otoño ")

