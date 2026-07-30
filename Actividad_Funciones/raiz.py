import math

def raiz_newton(n, tolerancia=1e-10):
    """Función que calcula la raíz cudrada de un número,
    usando el método de Newton"""
    if n < 0:
        raise ValueError("No se puede calcular raíz de negativo")
    estimacion = n / 2.0
    while True:
        nueva = 0.5 * (estimacion + n / estimacion)
        if abs(nueva - estimacion) < tolerancia:
            return nueva
        estimacion = nueva

try:
    #Pide al usuario un número a evaluar
    num = float(input("Número: "))
    #Calcula la primera respuesta con el uso de math
    r1 = math.sqrt(num)
    #Calcula la segunda respuesta con el uso de la función
    r2 = raiz_newton(num)
    #Imprime ambos resultados
    print(f"math.sqrt: {r1}, Newton: {r2:.10f}")
    #Si ambos resultados tienen suficiente similitud
    if abs(r1-r2) < 1e-9: 
        print("Resultados coinciden")
    else: #Si no
        print("Diferencia significativa")
#Si el usuario ingresa un número no válido, lanza error
except ValueError as e: 
    print("Error", e)