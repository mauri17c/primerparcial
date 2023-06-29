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