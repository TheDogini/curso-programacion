def es_palindromo(texto):
    """Función que determina si una cadena de texto
    es palíndroma o no, al igual que cuenta la cantidad
    de caracteres de la cadena sin espacios"""
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    return limpio == limpio[::-1], limpio
#Pide al usuario la frase a evaluar
entrada = input("Ingrese una frase: ")
#Manda a llamar la función
resultado, cadena_limpia = es_palindromo(entrada)

if resultado: #Si devuelve True
    print("Es un palindromo")
else: #Si devuelve False
    print("No es un palindromo")
#Imprime la longitud de la cadena limpia
print("Longitud de la cadena limpia:", len(cadena_limpia))