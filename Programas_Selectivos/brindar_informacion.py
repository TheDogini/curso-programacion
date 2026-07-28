#Se hace la pregunta al usuario
opcion = input("¿Sobre qué deseas conocer?: ").lower()

#Se selecciona de entre las entradas
match opcion:
    case "smiling friends":
        print("Caricatura para adultos con movimientos erraticos y chistes oscuros y crudos")
    case "hayley williams":
        print("Cantante principal de 'Paramore' y artista individual reconocida por su talento vocal")
    case "avengers":
        print("Película de superheroes basada en los comics de MARVEL")
    case "dr house":
        print("Serie de medicina protagonizada por el Dr. House y su equipo de médicos diagnósticos")
    case "escandalosos":
        print("Caricatura infantil que sigue la vida de tres osos que intentan vivir normalmente")
    case _:
        #Mensaje de error si el usuario introduce algún aspecto no soportado
        print("Error, información no encontrada")