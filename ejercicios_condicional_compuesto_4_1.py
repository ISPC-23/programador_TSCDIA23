import math

def ejercicio_1():
	lado1 = math.floor(float(input("Ingrese el valor del lado A: ")))
	lado2 = math.floor(float(input("Ingrese el valor del lado B: ")))
	lado3 = math.floor(float(input("Ingrese el valor del lado C: ")))
	if (lado1 == lado2):
		if (lado2 == lado3):
			result = "Equilátero"
		else:
			result = "Isóseles"
	elif (lado1 == lado3 or lado2 == lado3):
		result = "Isóseles"
	else:
		result = "Escaleno"
		
	print(f"Según los valores ingresados, el triangulo es {result}")


def ejercicio_2():
	importe = float(input("Ingrese el monto a pagar: "))
	print("Las opciones de pago son:")
	print("1 - Contado (10% descuento)")
	print("2 - Tarjeta (10% interés)")
	print("3 - Débito (5% descuento)")
	formaPago = input("Seleccione la forma de pago(1,2,3): ")
	print(f"Importe = {importe}")
	if (formaPago == "1"):
		descuento = importe / 10
		print(f"Descuento = {descuento}")
		total = importe - descuento
	elif (formaPago == "2"):
		interes = importe / 10
		print(f"Interés = {interes}")
		total = importe + interes
	elif (formaPago == "3"):
		descuento = importe / 20
		print(f"Descuento = {descuento}")
		total = importe - descuento
	else:
		print("Debe ingresar 1,2 ó 3. Intente de nuevo")
		return
	print(f"Total = {total}")


def ejercicio_3():
	num1 = math.floor(float(input("Ingrese el primer número: ")))
	num2 = math.floor(float(input("Ingrese el segundo número: ")))
	num3 = math.floor(float(input("Ingrese el tercer número: ")))
	if (num1 > num2):
		if (num1 > num3):
			mayor = num1
		else:
			mayor = num3
	else:
		if (num2 > num3):
			mayor = num2
		else:
			mayor = num3
	if ((mayor % 2) == 0):
		paridad = "par"
	else:
		paridad = "impar"
	print(f"El mayor es {mayor} y es {paridad}")


def ejercicio_4():
	diaSemana = ["Lunes", "Martes", "Miercoles", "Jueves",
				"Viernes", "Sabado", "Domingo"]
	numero = math.floor(float(input("Ingrese un número(1 al 7): ")))
	if (numero > 0 and numero < 8):
		print(f"El número {numero} corresponde al día {diaSemana[numero-1]}")
	else:
		print("Debe ingresar un número del 1 al 7. Intente de nuevo")


def ejercicio_5():
	meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
			"Junio", "Julio", "Agosto", "Septiembre",
			"Octubre", "Noviembre", "Diciembre"]
	numero = math.floor(float(input("Ingrese un número(1 al 12): ")))
	if (numero > 0 and numero < 13):
		print(f"El número {numero} corresponde al mes {meses[numero-1]}")
	else:
		print("Debe ingresar un número del 1 al 12. Intente de nuevo")


#Fin de definiciones
#Ejecutar menu
ejercicio = 1

print("\n1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.")
print("\n2. Permitir al usuario simular el pago ingresando el importe y la forma de pago.")
print("\n3. Leer tres números, mostrar el mayor y decir si es par o impar.")
print("\n4. Pedir un número del 1 al 7 y decir el día de la semana correspondiente.")
print("\n5. Pedir un número del 1 al 12 y decir el mes correspondiente.")

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
		print("\nIngrese un numero de ejercicio válido 1-5. O ingrese cero para salir")

