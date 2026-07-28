#Se obtiene el mes a evaluar
mes = input("¿Cuál es el mes actual?: ").lower()

#Se asocia el mes a una estación usando match-case
match mes:
    case "diciembre":
        estacion = "Invierno"
    case "enero":
        estacion = "Invierno"
    case "febrero":
        estacion = "Invierno"
    case "marzo":
        estacion = "Primavera"
    case "abril":
        estacion = "Primavera"
    case "mayo":
        estacion = "Primavera"
    case "junio":
        estacion = "Verano"
    case "julio":
        estacion = "Verano"
    case "agosto":
        estacion = "Verano"
    case "septiembre":
        estacion = "Otoño"
    case "octubre":
        estacion = "Otoño"
    case "noviembre":
        estacion = "Otoño"
    case _:
        #Se asigna un valor nulo si el mes no coincide con ningún caso
        estacion = ""

if estacion == "":
    #Mensaje de error
    print("Error, mes inválido")
else:
    #Mensaje con la estacion actual
    print("La estación actual es:", estacion)