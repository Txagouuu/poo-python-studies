class ContaBancaria:
    ContaBancaria = []
    def __init__(self, titular='', saldo=0.0):
        self.titular = titular
        self.saldo = saldo
        self._conta = False #atributo protegido para indicar se a conta está ativa
    
    def __str__(self,titular='', saldo=0.0,):
        return f'Conta de {self.titular} - Saldo: R${self.saldo:.2f} {"(Ativa)" if self._conta else "(Inativa)"}'

    @classmethod
    def ativar_conta(cls,conta):
        conta._conta = True
        return f'Conta de {conta.titular} ativada com sucesso!'
    
conta1 = ContaBancaria('João Silva', 1500.00)
conta2 = ContaBancaria('Maria Oliveira', 2500.00)


ContaBancaria.ativar_conta(conta1)
print(conta1)  # Verifica se a conta foi ativada

class ContaBancariaPythonica:
    def __init__(self, titular='', saldo=0.0):
        self._titular = ''
        self._saldo = 0.0
        self._conta = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo 
    
    @property
    def conta_ativa(self):
        return self._conta
    
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")

# 6) Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

# 7) Crie um método de classe para a conta `ClienteBanco`.
class ClienteBanco:
    def __init__(self,titular,saldo_inicial=0.0):

        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo


    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")