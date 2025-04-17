def leer_entero(msg):
    try:
        texto = input(msg)
        return int(texto)
    except ValueError as e:
        raise ValueError("Dato numérico inválido") from e


def dividir_dos_entradas():
    try:
        num = leer_entero("Ingresa numerador: ")
        den = leer_entero("Ingresa denominador: ")

        resultado = num / den

    except ZeroDivisionError:
        print("No se puede dividir por 0.")

    except ValueError as err:
        print(err)

    else:
        print("Resultado =", resultado)

    finally:
        print("Fin del cálculo.")


# Programa principal
dividir_dos_entradas()

