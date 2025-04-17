try:
	a = int(input("Ingresa el primer valor: "))
	b = int(input("Ingresa el segundo valor "))

	resultado = a/b

except  ZeroDivisionError:

	print("No se puede divdir por cero")

except ValueError:

	print("Debes de ingresar un numero valido")

else: 
	print(f"La division de tus numeros es: {resultado}")

finally:
	print(f"Operacion finalizada")


