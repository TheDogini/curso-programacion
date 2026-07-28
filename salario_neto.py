salario_bruto = float(input("¿Cuál es tu salario bruto?: ")) #Obtiene el salario bruto
impuestos = float(input("¿Cuál es tu porcentaje de impuestos?: ")) #Obtiene los impuestos
deducciones = float(input("¿De cuánto son tus deducciones?: ")) #Obtiene las deducciones

#Se realiza el calculo del salario neto:
salario_neto = (salario_bruto - (salario_bruto * (impuestos/100))) - deducciones 

print("Tu salario neto es de:", salario_neto) #Imprime el resultado