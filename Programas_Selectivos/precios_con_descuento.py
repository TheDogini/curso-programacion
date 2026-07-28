#Se obtiene el precio a evaluar
precio_inicial = float(input("¿Cuál es el precio del artículo?: "))

#Se hacen comparaciones con rangos de valores para aplicar un descuento específico
if (precio_inicial > 0 and precio_inicial <= 100):
    descuento = 0
    #Se calcula el precio final
    precio_final = precio_inicial - (precio_inicial * (descuento / 100))
    #Se imprime el porcentaje de descuento aplicado
    print("Descuento correspondiente: ", descuento, "%", sep='')
    #Se imprime el precio final con el descuento aplicado
    print("El precio final del artículo con el descuento aplicado es de:", precio_final)
elif (precio_inicial > 100 and precio_inicial <= 200):
    descuento = 5
    #Se calcula el precio final
    precio_final = precio_inicial - (precio_inicial * (descuento / 100))
    #Se imprime el porcentaje de descuento aplicado
    print("Descuento correspondiente: ", descuento, "%", sep='')
    #Se imprime el precio final con el descuento aplicado
    print("El precio final del artículo con el descuento aplicado es de:", precio_final)
elif (precio_inicial > 200 and precio_inicial <= 500):
    descuento = 10
    #Se calcula el precio final
    precio_final = precio_inicial - (precio_inicial * (descuento / 100))
    #Se imprime el porcentaje de descuento aplicado
    print("Descuento correspondiente: ", descuento, "%", sep='')
    #Se imprime el precio final con el descuento aplicado
    print("El precio final del artículo con el descuento aplicado es de:", precio_final)
elif (precio_inicial > 500):
    descuento = 15
    #Se calcula el precio final
    precio_final = precio_inicial - (precio_inicial * (descuento / 100))
    #Se imprime el porcentaje de descuento aplicado
    print("Descuento correspondiente: ", descuento, "%", sep='')
    #Se imprime el precio final con el descuento aplicado
    print("El precio final del artículo con el descuento aplicado es de:", precio_final)
else:
    print("Error, precio no válido")
    