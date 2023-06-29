# actividad 1
#Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el
#año de nacimiento

anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

anio_actual = 2023
edad_actual = anio_actual - anio_nacimiento

print("Tu edad actual es:", edad_actual)

edad_cumplira = anio_actual - anio_nacimiento + 1

print("Este año cumplirás:", edad_cumplira, "años")