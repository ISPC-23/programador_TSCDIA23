import math

def ejercicio_1():
	son_pares = 0
	sum_pares = 0

	for x in range(4):
		numero_ingresado = math.floor(float(input("Ingrese un número: ")))
		if numero_ingresado % 2 == 0:
			son_pares += 1
			sum_pares += numero_ingresado

	print(f"\nSe ingresaron {son_pares} números pares y {4-son_pares} impares")
	print(f"\nLa sumatoria de los numeros pares es {sum_pares}")


def ejercicio_2():
	cantidad_max100 = 0
	cantidad_min100 = 0
	numero_ingresado = math.floor(float(input("Ingrese un número: ")))
	numero_min = numero_ingresado
	numero_max = numero_ingresado

	for x in range(10):
		if numero_ingresado > 100:
			cantidad_max100 += 1
		if numero_ingresado < 100:
			cantidad_min100 += 1
		if numero_ingresado > numero_max:
			numero_max = numero_ingresado
		if numero_ingresado < numero_min:
			numero_min = numero_ingresado
		if x < 9:
			numero_ingresado = math.floor(float(input("Ingrese un número: ")))
	
	print(f"\nSe ingresaron {cantidad_max100} mayores a 100")
	print(f"\nSe ingresaron {cantidad_min100} menores a 100")
	print(f"\nEl máximo es {numero_max}")
	print(f"\nEl minimo es {numero_min}")


def ejercicio_3():
	mujeres = 0
	mayores = 0

	for x in range(15):
		print(f"\nDatos de la persona {x+1}")
		edad = math.floor(float(input("Ingrese la edad: ")))
		sexo = input("Ingrese sexo (f/m): ")
		if sexo == "f":
			mujeres += 1
		if edad >= 16:
			mayores += 1

	print(f"\nSe ingresaron {mujeres} mujeres y {15 - mujeres} varones")
	print(f"\nDe los cuales {mayores} son mayores y {15 - mayores} son menores de edad")


def ejercicio_4():
	sum_positivos = 0
	numeros = []
	
	for x in range(10):
		numero_ingresado = math.floor(float(input("Ingrese un número: ")))
		if numero_ingresado > 0:
			numeros.append(numero_ingresado)
	
	print("Los números positivos ingresados son:")
	for num in numeros:
		print(num)

	print(f"\nY la sumatoria es: {sum(numeros)}")


def ejercicio_5():
	numeros = []

	for x in range(15):
		numero_ingresado = math.floor(float(input("Ingrese un número: ")))
		numeros.append(numero_ingresado)

	print("\nLos números ingresados convertido a positivo")	
	for num in numeros:
		print(abs(num))

#Fin de definiciones
#Ejecutar menu
ejercicio = 1

print("\n1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.")
print("\n2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.")
print("\n3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.")
print("\n4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.")
print("\n5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.")

while ejercicio != 0:
	ejercicio = math.floor(float(input("\nIngrese el número de ejercicio a ejecutar (0=salir): ")))
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
	elif ejercicio == 0:
		print("\nGracias por ejecutar mis ejercicios")
	else:
		print("\nIngrese un número de ejercicio válido 1-5. O ingrese cero para salir")

