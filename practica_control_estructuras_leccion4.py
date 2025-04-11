temperatura = int(input("ingresa la temperatura actual: "))

if temperatura < 10:
	print("hacce frio")
elif temperatura >= 10 and temperatura <= 25:
	print("la tenperatura es templada")
else:
	print("hace calor")
