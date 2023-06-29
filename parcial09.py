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
