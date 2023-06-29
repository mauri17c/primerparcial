#actividad 7
#Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de
#horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
#a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
#b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
#c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
#d. El programa debe mostrar elsalario anual bruto, el monto anual de bonificaciones, el monto anual
#a descontarse y las horas trabajadas en todo el año

SALARIO_POR_HORA = 10000
HORAS_TRABAJADAS_POR_MES = 160
DESCUENTO_1 = 0.01
DESCUENTO_2 = 0.03
DESCUENTO_3 = 0.05

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas al mes: "))

salario_mensual = horas_trabajadas * SALARIO_POR_HORA
salario_anual = salario_mensual * 12

if salario_anual > 2000000:
    
    descuento = salario_anual * DESCUENTO_3 
    print("el descuento fue: ",descuento)
    salario_anual = salario_anual - descuento
    print("el salario anual es: ",salario_anual)

elif salario_anual >= 1000000 and salario_anual <= 2000000:

    descuento = salario_anual * DESCUENTO_1
    print("el descuento fue: ",descuento)
    salario_anual = salario_anual - descuento
    print("el salario anual es: ",salario_anual)

else:

    descuento = salario_anual * DESCUENTO_2
    print("el descuento fue: ",descuento)
    salario_anual = salario_anual - descuento
    print("el salario anual es: ",salario_anual)