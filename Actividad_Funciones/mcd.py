import math

def mcd(a, b):
    """
    Función que determina el mcd de dos números,
    usando el algoritmo de Euclides
    """
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a
#Pide al usuario los números a evaluar
num_1 = int(input("Primer número: "))
num_2 = int(input("Segundo número: "))

#Calcula el resultado con la función
resultado = mcd(num_1, num_2)
#Calcula el resultado con la librería 'math'
resultado_math = math.gcd(num_1, num_2)

#Imprime los resultados
print(f"MCD calculado: {resultado}")
print(f"MCD con math.gcd: {resultado_math}")
print("Los resultados sí coinciden" if resultado == resultado_math else "No coinciden")

#Evalúa si los resultados coinciden o no
if num_1 == 0 and num_2 == 0:
    print("Caso especial: ambos números son cero")
else: 
    print("Programa terminado")