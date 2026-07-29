#Imprime el título del código
print("Números divisibles entre 3 y 5 (1-100):")
for i in range(1, 101): #Cicla los números del 1 al 100
    if (i % 3 == 0 and i % 5 == 0): #Si la condición se cumple...
        print(i) #Imprime el número