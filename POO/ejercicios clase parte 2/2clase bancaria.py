class CuentaBancaria:
    titular:str
    saldo: float
    numeroDeCuenta: str

    def __init__(self,titular: str, saldo: float, numeroDeCuenta: str):
        self.titular = titular
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta

    def depositar(self, cantidad: float):
        self.saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        return self.saldo


cuenta1 = CuentaBancaria('titular1', 1000, "123456789")
cuenta1.depositar(500)
print("Saldo después del depósito:", cuenta1.consultar_saldo())
cuenta1.retirar(300)
print("Saldo después del retiro:", cuenta1.consultar_saldo())
cuenta1.retirar(1500) 