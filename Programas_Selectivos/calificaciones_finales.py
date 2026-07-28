#Obtiene los valores necesarios
parciales = float(input("Calificación de los parciales: ")) 
proyecto = float(input("Calificación del proyecto: "))
examen = float(input("Calificación del exámen: "))

#Verifica que todos los valores sean válidos
if (parciales < 0 or parciales > 100):
    print("Error, calificación de los parciales incorrecta")
elif (proyecto < 0 or proyecto > 100):
    print("Error, calificación del proyecto incorrecta")
elif (examen < 0 or examen > 100):
    print("Error, calificación del examen incorrecta")
else:
    #Calcula el promedio final con los porcentajes acordados
    promedio = (parciales * 0.4) + (proyecto * 0.3) + (examen * 0.3)
    print("El promedio final es de:", promedio)