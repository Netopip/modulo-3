
class Banco:
    def __init__(self):
        self.contas={}
    
    def adicionar_conta(self,titular,saldo):
        pass
    
    def transferir_dinheiro(self):
        pass
    
class ContaBancaria:
    def __init__(self,titular:str,saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self,valor):
        try:
            valor = float(valor)
            if valor <= 0.1:
                return f'Valor não pode ser menor que R$ 0,01'
            else:
                self.__saldo += valor
                return f'Saldo atualizado com sucesso!'
        except:
            return f'Digite um valor válido'
            
    
    def sacar(self,valor):
        try:
            valor = float(valor)
            if valor < 0.1:
                return f'Não é possível sacar esse valor!'
            elif valor > self.__saldo:
                return f'Saldo insuficiente!'
            else:
                self.__saldo -= valor
                return f'Saque de {valor} realizado com sucesso!'
        except:
            return f'Digite um valor válido'
    
    def exibir_saldo(self):
        return self.__saldo
    
    
    def __str__(self):
        return f'Titular: {self.titular}\nSaldo: {self.__saldo}'
    
conta1 = ContaBancaria(titular='Neto',saldo=23.50)
print(conta1)
