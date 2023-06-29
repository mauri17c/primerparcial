#actividad 5
#Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre
#por pantalla el resultado, considerando lo siguiente:
#a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
#b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
#c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas este mes: "))

if horas_trabajadas > 120:
    valor_hora = 1500
elif horas_trabajadas >= 80:
    valor_hora = 1300
else:
    valor_hora = 1100

sueldo = horas_trabajadas * valor_hora

print("El sueldo del empleado es: $" + str(sueldo))