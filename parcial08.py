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
