def main():
    """Función cíclica indetermindada que convierte
    las palabras ingresadas a mayúsculas, y cuenta
    la cantidad de palabras. Termina el programa
    con un espacio"""
    contador = 0
    while True:
        #Pide la palabra al usuario
        entrada = input("Palabra o número (espacio termina): ")
        if entrada == " ": #Si es un espacio, termina el programa
            break
        try:
            if entrada.isdigit(): #Si es un número, lo convierte a str
                entrada = str(entrada)
            print(entrada.upper()) #imprime la palabra en mayúsculas
            contador += 1 #Añade 1 al contador
        except Exception as e:
            print("Error: ", e)
    #Imprime los resultados
    print("Programa terminado")
    print("Cantidad de palabras contadas:", contador)
main()