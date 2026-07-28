#Se obtiene la cantidad de pesos a convertir
pesos = float(input("¿Cuántos pesos mexicanos deseas convertir?: "))

#Se pregunta por la divisa a transformar
opcion = input("¿A qué deseas convertirlos? (USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS): ").lower()

#Se hacen los calculos correspondientes para cada divisa
match opcion:
    case "usd":
        valor_final = pesos * 0.057
        print("Sus", pesos, "pesos equivalen a", valor_final, "USD")
    case "eur":
        valor_final = pesos * 0.050
        print("Sus", pesos, "pesos equivalen a", valor_final, "EUR")
    case "thb":
        valor_final = pesos * 1.92
        print("Sus", pesos, "pesos equivalen a", valor_final, "THB")
    case "jpy":
        valor_final = pesos * 9.38
        print("Sus", pesos, "pesos equivalen a", valor_final, "JPY")
    case "krw":
        valor_final = pesos * 83.89
        print("Sus", pesos, "pesos equivalen a", valor_final, "KRW")
    case "aud":
        valor_final = pesos * 0.082
        print("Sus", pesos, "pesos equivalen a", valor_final, "AUD")
    case "pen":
        valor_final = pesos * 0.19
        print("Sus", pesos, "pesos equivalen a", valor_final, "PEN")
    case "cad":
        valor_final = pesos * 0.081
        print("Sus", pesos, "pesos equivalen a", valor_final, "CAD")
    case "ves":
        valor_final = pesos * 42.45
        print("Sus", pesos, "pesos equivalen a", valor_final, "VES")
    case "ars":
        valor_final = pesos * 85.71
        print("Sus", pesos, "pesos equivalen a", valor_final, "ARS")
    case _:
        #Mensaje de error si la divisa es inválida
        print("Error, divisa inválida")