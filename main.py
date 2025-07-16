from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = 0
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

@classmethod
def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

@property
def saldo(self):
    return self._saldo

@property
def numero(self):
    return self._numero

@property
def agencia(self):
    return self._agencia

@property
def cliente(self):
    return self._cliente

@property
def historico(self):
    return self._historico

def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("Saldo Insuficente")
    elif valor > 0:
        self._saldo -= valor
        print("Saque Realizado")
        return True
    else:
        print("Valor Invalido")
    
    return False

def depositar(self, valor):
    if valor > 0:
        self._saldo += valor
        print("Deposito Realizado")
        return True
    else:
        print("Operação Falhou")
        return False   
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques =3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self._historico.transacoes if
             transacao["tipo"] == "Saque"]
        )
    
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print("Limite de saque excedido")
        elif excedeu_saques:
            print("Numero de saques excedido")
        else:
            return sacar(valor)

        return False
    
    def __str__(self):
        return f"""
            Agencia: {self._agencia}
            C/C: {self._numero}
            Titular: {self._cliente.nome}"""
    
