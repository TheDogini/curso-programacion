def es_primo(n):
    """Función que determina si el número
    ingresado por el usuario es primo,
    con un caso especial si el número es 2"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range (3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
#Pide el número a evaluar
num = int(input("Ingrese un número: "))
#Llama a la función
if es_primo(num): #Si devuelve True
    print("Es primo")
else: #Si devuelve False
    print("No es primo")