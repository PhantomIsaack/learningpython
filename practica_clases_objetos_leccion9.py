class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        print("La nueva velocidad es:", self.velocidad)

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0  # Evitamos que la velocidad sea negativa
        print("La nueva velocidad es:", self.velocidad)

    def mostrar_estado(self):
        print(f"La marca es: {self.marca}\nCon el modelo: {self.modelo}\nVa a una velocidad de: {self.velocidad} km/h")

# Creación de una instancia y demostración de funcionamiento
coche1 = Coche("BVW", "V8", 150)
coche1.mostrar_estado()
coche1.acelerar(50)   # Aumenta la velocidad
coche1.frenar(50)      # Disminuye la velocidad

