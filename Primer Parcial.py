# actividad 1
#Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el
#año de nacimiento

anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

anio_actual = 2023
edad_actual = anio_actual - anio_nacimiento

print("Tu edad actual es:", edad_actual)

edad_cumplira = anio_actual - anio_nacimiento + 1

print("Este año cumplirás:", edad_cumplira, "años")

# actividad 2
#Escribe un programa que calcule el área y el perímetro de un cuadrado y muestre los resultados (indicando
#cuál es cuál) por pantalla.

lado = int(input("Ingresa la longitud del lado del cuadrado: "))

area = lado ** 2
perimetro = lado * 4

print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)

#actividad 3
#Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El
#programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).

tipo_cambio = float(input("Ingresa el tipo de cambio a convertir: "))
dolares = float(input("Ingresa la cantidad de dólares a convertir: "))
pesos = dolares * tipo_cambio
print("$" + str(dolares) + " dólares son $" + str(pesos) + " pesos.")

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

#avtividad 6
#Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto
#(bruto + bonif), considerando:
#a. Si trabajo más de 120hs, la bonificación es de %18
#b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
#c. Si trabajo menos de 80 horas, la bonificación es de %13

horas = int(input("ingrese cuantas horas trabajo en el mes: "))
if horas < 120:
     multiplicacion = horas * 1300 
     print("A usted le corresponde: $", multiplicacion)
elif horas>=120 and horas <120:
     multiplicacion = horas * 1500 
     print("A ested le corresponde $", multiplicacion) 
elif horas >120:
      print("inexistente")

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
elif salario_anual >= 1000000 and salario_anual <= 2000000:
    descuento = salario_anual * DESCUENTO_2
else:
    descuento = salario_anual * DESCUENTO_1

print("Salario anual bruto: $", salario_anual)
print("Descuento anual: $", descuento)

#actividad 8
#Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas

cont = 1
while(cont<= 5):
  nombre = input("Ingrese su nombre:")
  apellido = input("Ingrese su apellido:")
  edad = input("Ingrese sus edad:")
 
  print(F"(nombre), (apellido) (edad) años")
  cont=cont+1
  print(cont)
else:
  print("Ya se cargaron las 5 personas")

#actividad 9
#Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de
#personas ingresada por el usuario

cantidad_personas =int(input("ingrese la cantidad de personas: "))
while(cantidad_personas):
     nombre=input("Ingrese su nombre ")
     apellido=input("Ingrese su apellido")
     edad=input("Ingrese su edad ")
     print("nombre:" , (nombre),",apellido:",(apellido),",edad:",str(edad))
     cantidad_personas =cantidad_personas-1

     print("nombre:"(nombre ))
     print("apellido:",(apellido))
     print("edad:",(edad))
else:
    print("fin del programa")

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

#actividad 12
#Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no
#hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas

estudiante= int(input("ingrese las edades: "))
suma_general =0
contador =0

while contador < estudiante:
    notas = float(input(" El total de las personas ingresadas: "))
    suma_general += notas
    contador=contador+1

promedio = suma_general / estudiante
print("promedio es:",(promedio))
