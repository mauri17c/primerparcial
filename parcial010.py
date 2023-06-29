#actividad 10
#Escribe un programa que calcule el promedio general de una clase.

estudiante= int(input("cuantos alumnos desea ingresar: "))
suma_general=0
contador=0

while contador < estudiante:
     notas = float(input("ingrese notas del estudiante: "))
     suma_general += notas
     contador=contador+1

promedio = suma_general / estudiante
print("el promedio general de la clase es:",(promedio))