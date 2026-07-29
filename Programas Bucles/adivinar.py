import random
#Asgina una variable con un número aleatorio
winner = random.randint(1, 100)
#Cicla infinitamente hasta que se adivine el número
while True:
    #Pregunta al usuario por su conjetura
    numero = int(input("Intenta adivinar el número (1-100): "))
    if numero == winner: #Si lo adivina, se rompe el ciclo
        print("Correcto, lo adivinaste!!")
        break
    else: #Si no, el ciclo continúa
        print("Incorrecto, intenta de nuevo")
#Imprime un mensaje final con el número ganador
print("El número era:", winner)