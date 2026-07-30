def reemplazar_manual(texto, viejo, nuevo):
    """Función para reemplazar un caracter de una cadena de texto,
    especificando el caracter viejo y el nuevo"""
    if len(viejo) != 1 or len(nuevo) != 1:
        return texto, 0
    resultado = ""
    contador = 0
    for letra in texto:
        if letra == viejo:
            resultado += nuevo
            contador += 1
        else:
            resultado += letra
    return resultado, contador
#Pide al usuario la frase inicial
texto = input("Cadena: ")
#Pregunta por el caracter a reemplazar
car_viejo = input("Caracter a reeemplazar: ")
#Pregunta por el caracter nuevo
car_nuevo = input("Caracter nuevo: ")

#Si el usuario ingresa más de un caracter, lanza error
if len(car_viejo) != 1 or len(car_nuevo) != 1:
    print("Debe inrgesar solo un caracter")
else: #Sino, lo modifica con la función manual, y con "replace"
    texto_mod, num = reemplazar_manual(texto, car_viejo, car_nuevo)
    texto_mod2 = texto.replace(car_viejo, car_nuevo)
    print("Manual:", texto_mod, "|Reemplazos:", num)
    print("Con replace:", texto_mod2)
    if texto_mod == texto_mod2:
        print("Correcto")