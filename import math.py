import math

# Declaración del autor del trabajo
autor = "Miguel Ángel Rivillas"

def mostrar_autor():
    print("\nTrabajo realizado por:")
    print(f"- {autor}\n")

# Función para la opción 1
def opcion_1():
    numeros = []
    while len(numeros) < 2:
        entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            if len(numeros) < 2:
                print("Debe ingresar al menos 2 números.")
                continue
            else:
                break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    print("\nResultados:")
    print(f"Seno del segundo número ({numeros[1]}): {math.sin(numeros[1])}")
    print(f"Tangente del primer número ({numeros[0]}): {math.tan(numeros[0])}")
    print(f"Residuo entre {numeros[0]} y {numeros[1]}: {numeros[0] % numeros[1]}")
    print("Todos los números ingresados:", numeros)

    multiplos_de_3 = [n for n in numeros if n % 3 == 0]
    print("Números múltiplos de 3:", multiplos_de_3 if multiplos_de_3 else "Ninguno")

# Funciones para la opción 2
def contar_caracteres():
    texto = input("Ingrese un texto: ")
    print(f"El texto tiene {len(texto)} caracteres.")

def calcular_factorial():
    try:
        numero = int(input("Ingrese un número entero para calcular su factorial: "))
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

def sumar_hasta():
    try:
        numero = int(input("Ingrese un número entero para sumar hasta ese valor: "))
        suma = sum(range(1, numero + 1))
        print(f"La suma de los números desde 1 hasta {numero} es: {suma}")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

def opcion_2():
    while True:
        print("\n--- Submenú Opción 2 ---")
        print("1. Contar caracteres de un texto")
        print("2. Calcular factorial de un número")
        print("3. Sumar números hasta un valor dado")
        print("4. Volver al menú principal")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            contar_caracteres()
        elif eleccion == "2":
            calcular_factorial()
        elif eleccion == "3":
            sumar_hasta()
        elif eleccion == "4":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Menú principal
def menu_principal():
    mostrar_autor()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Operaciones con números (60%)")
        print("2. Operaciones con texto y números (40%)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
menu_principal()