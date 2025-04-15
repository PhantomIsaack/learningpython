nombre_usuario = input("Ingrese su nombre por favor: ")
reseña = input("Escribe una reseña: ")

archivo  = open("datos.txt", "w")
archivo.write(f"Tu nombre es: {nombre_usuario} \n{reseña}")
archivo.close

archivo = open ("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
