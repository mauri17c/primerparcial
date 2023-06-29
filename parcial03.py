#actividad 3
#Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El
#programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).

tipo_cambio = float(input("Ingresa el tipo de cambio a convertir: "))
dolares = float(input("Ingresa la cantidad de dólares a convertir: "))
pesos = dolares * tipo_cambio
print("$" + str(dolares) + " dólares son $" + str(pesos) + " pesos.")