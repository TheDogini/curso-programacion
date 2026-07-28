#Obtiene la calificación a evaluar
calificacion = float(input("Calificación obtenida: "))

#Asocia un rango de calificación con una letra
if (calificacion <= 100 and calificacion >= 90):
    letra = "A"
    print("Letra correspondiente:", letra)
elif (calificacion < 90 and calificacion >= 80):
    letra = "B"
    print("Letra correspondiente:", letra)
elif (calificacion < 80 and calificacion >= 70):
    letra = "C"
    print("Letra correspondiente:", letra)
elif (calificacion < 70 and calificacion >= 60):
    letra = "D"
    print("Letra correspondiente:", letra)
elif (calificacion < 60 and calificacion >= 0):
    letra = "F"
    print("Letra correspondiente:", letra)
else:
    #Si la calificación sale del rango permmitido, muestra un error
    print("Error, calificación no válida")