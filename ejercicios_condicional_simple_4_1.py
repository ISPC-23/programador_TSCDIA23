import math

def ejercicio_1():
	let_1 = input("Ingrese la primer letra: ")
	let_2 = input("Ingrese la segunda letra: ")
	if (let_1 == let_2):
		print(f'Las letras "{let_1}" y "{let_2}" son IGUALES')
	else:
		print(f'Las letras "{let_1}" y "{let_2}" son DIFERENTES')


def ejercicio_2():
	pal_1 = input("Ingrese la primer palabra: ")
	pal_2 = input("Ingrese la segunda palabra: ")
	if (pal_1 == pal_2):
		print(f'Las palabras "{pal_1}" y "{pal_2}" son IGUALES')
	else:
		print(f'Las palabras "{pal_1}" y "{pal_2}" son DIFERENTES')


def ejercicio_3():
	genero = input("Ingrese género ('f'/'m'): ").lower()
	if (genero == "f"):
		print("vota en mesa femenina")
	elif (genero == "m"):
		print("vota en mesa masculina")
	else:
		print("Debe ingresar 'f' o 'm', intente de nuevo")


def ejercicio_4():
	num_1 = math.floor(float(input("Ingrese el primer número: ")))
	num_2 = math.floor(float(input("Ingrese el segundo número: ")))
	if (num_1 >= num_2):
		print(f'El mayor es el número "{num_1}"')
	else:
		print(f'El mayor es el número "{num_2}"')


def ejercicio_5():
	cotizacion = 500
	
	print("Ingrese '0' para usar cotización=500 o un número mayor para usar ese valor" )
	nueva_cot = math.floor(float(input("Nuevo valor: ")))
	if (nueva_cot):
		cotizacion = nueva_cot
	print(f'La cotización actual es "{cotizacion}"\n')
	print("1. Cambio de Dólares a Pesos")
	print("2. Cambio de Pesos a Dólares")
	modo = input("Ingrese el número para seleccionar el cambio: ")
	if (modo == '1'):
		print("Eligió cambiar Dólares a Pesos")
		cantidad = math.floor(float(input("Cuantos Dólares quiere cambiar? ")))
		cambio = cantidad * cotizacion
		print(f'Cambio de {cantidad} Dólares a {cambio} Pesos')
	elif (modo == '2'):
		print("Eligió cambiar Pesos a Dólares")
		cantidad = math.floor(float(input("Cuantos Pesos quiere cambiar? ")))
		cambio = cantidad / cotizacion
		print(f'Cambio de {cantidad} Pesos a {cambio} Dólares')
	else:
		print("Debe ingresar '1' o '2', intente de nuevo")


def ejercicio_6():
	edad = math.floor(float(input("Ingrese su edad: ")))
	if (edad > 16):
		print(f'Con {edad} años "PUEDE VOTAR"')
	else:
		print(f'Con {edad} años "NO puede votar"')




#Fin de definiciones
#Ejecutar menu
ejercicio = 1

print("\n1. Ingresar 2 letras y verificar si son iguales.")
print("\n2. Decidir si dos palabras son iguales o diferentes.")
print("\n3. Ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.")
print("\n4. Ingresar dos números y diga cuál es el mayor.")
print("\n5. Cambio pesos a dólares, o de dólares a pesos.")
print("\n6. Ingrese su edad. Si es mayor de 16 años, mensaje “puede votar”, sino “no vota”.")


while ejercicio != 0:
	ejercicio = math.floor(float(input("\nIngrese el número de ejercicio a ejecutar: ")))
	if ejercicio == 1:
		ejercicio_1()
	elif ejercicio == 2:
		ejercicio_2()
	elif ejercicio == 3:
		ejercicio_3()
	elif ejercicio == 4:
		ejercicio_4()
	elif ejercicio == 5:
		ejercicio_5()
	elif ejercicio == 6:
		ejercicio_6()
	elif ejercicio == 0:
		print("\nGracias por ejecutar mis ejercicios")
	else:
		print("\nIngrese un número de ejercicio valido '1-6'. Ingrese '0'(cero) para salir")
