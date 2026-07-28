edad = int(input("¿Cuántos años tienes?: ")) #Pregunta por la edad del usuario
if (edad <= 17): #Valida aún no alcanza la mayoría de edad
    print("Eres menor de edad, no puedes votar")
else: #Si la alcanza, da el mensaje positivo
    print("Eres mayor de edad, puedes votar")