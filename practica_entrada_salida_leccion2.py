nombre = input("¿Cuál es tu nombre?")
edad = input("¿Cuántos años tienes?")
#como input almacena el dato  como str lo tenemos que converir si trabajamos con numero
edad = int(edad)

estatura = input("¿Cuál es tu estatura?")
#convertimos el dato
estatura = float(estatura)

#imprimimos los valores con ayuda de f-string
print(f"Hola, {nombre}. Tienes {edad}, y mides {estatura}")
