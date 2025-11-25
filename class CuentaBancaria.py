class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular          # Atributo privado
        self.__saldo = saldo_inicial      # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_saldo(self):
        print(f"Titular: {self.__titular} - Saldo actual: ${self.__saldo}")

# Ejemplo de uso
cuenta = CuentaBancaria("Miguel Ángel", 1000)
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.__saldo = 999999  # No tiene efecto: atributo privado
cuenta.mostrar_saldo()