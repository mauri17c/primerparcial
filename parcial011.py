#actividad 11
#.Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
#a.Si es número es par o impar.
#b.Cuanto es la suma total de todos los números mostrados.
#c.Cuanto es la suma total de todos los números pares mostrados.
#d.Cuanto es la suma total de todos los números impares mostrados

numero =1
suma_total =0
suma_pares =0
suma_impares =0

while numero <= 10:
    print(numero)

    if numero % 2 == 0:
        print("es un numero par.")
        suma_pares += numero

    else:
        print("es un numero impar")
        suma_impares += numero 

    suma_total += numero

numero += 1

print("la suma total es:", suma_total)
print("la suma de los numeros pares es:", suma_pares)
print("la suma de los numeros impares es:", suma_impares)