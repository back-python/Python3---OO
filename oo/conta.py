class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('construindo um objeto ...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def tirar_extrato(self):
        print('Saldo de R$ {} do titular {}'.format(self.saldo, self.titular))

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor inválido!')

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
        else:
            print('Valor inválido!')

    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, novo_valor):
        self.__saldo = novo_valor

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
