#actividad 4
#Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
#indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)

nota1 = float(input("Ingresa la nota del primer parcial: "))
nota2 = float(input("Ingresa la nota del segundo parcial: "))
nota3 = float(input("Ingresa la nota del tercer parcial: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 6:
    print("El promedio final es:",promedio,". Aprobado.")
else:
    print("El promedio final es:",promedio,". Debe recursar la materia.")