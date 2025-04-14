#se piden las numeros y se almacenan en las variables
a = int(input("ingresa un numero: "))
b = int(input("ingresa otro numero: "))

#variable para a opcion
op = input("Teclea el signo con el que se ejecute tus numeros: +, -, *, /: ")

#se construyen  las funciones
def sumar(a, b):
	resultado = a + b
	return resultado
def restar(a,b):
	resultado = a-b
	return resultado
def multiplicar (a,b):
	resultado = a*b
	return resultado
def dividir(a,b):
	resultado = a/b
	return resultado
#ejecucion de las opciones
if op == "+":
	suma = sumar (a,b)
	print (f"La suma es: {suma}")
elif op == "-":
	resta = restar(a,b)
	print(f"La resta es: {resta}")
elif op == "*":
	multiplicacion = multiplicar(a,b)
	print(f"La multiplicacion es: {multiplicacion}")
elif op == "/":
	division = dividir(a,b)
	print(f"La division es: {division}")
else :
	print("No se reconocio el caracter")
