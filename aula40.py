from abc import ABC,abstractmethod

class Contas(ABC):
    def __init__(self) -> None:
        self.saldo = 0
    
    @abstractmethod
    def sacar(self):
        ...

    def deposito(self,valor:float) -> float:
        self.saldo += valor
        return self.saldo



class ContaPoupanca(Contas):
    def __init__(self) -> None:
        self.agencia = "2224"
        self.numero_conta = "1"
        super().__init__()


    def sacar(self,valor:float) -> float:
        calculo = self.saldo - valor
        self.saldo = calculo
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        atrrs = f"{self.agencia},{self.numero_conta}"
        return f"{class_name}{atrrs}"


class ContaCorrente(Contas):
    def __init__(self) -> None:
        self.agencia = "2324"
        self.numero_conta = "2"
        super().__init__()

    def verificar_valor_extra(self) -> None:
        if self.saldo < 0:
            self.saldo += 100
            print("seu saldo foi atualizado")
        else:
            print("seu saldo nao esgotou")

    def sacar(self,valor:float) -> float:
        if self.saldo <= 0:
            raise ValueError("seu saldo esta zerado")
        else:
            calculo = self.saldo - valor
            self.saldo = calculo
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        atrrs = f"{self.agencia},{self.numero_conta}"
        return f"{class_name}{atrrs}"
    

class Pessoa:
    def __init__(self,*nome) -> None:
        self.nome = nome
        

class Cliente(Pessoa):
    def __init__(self, *nome) -> None:
        self.valores_contas = []
        super().__init__(*nome)

    def inserir_conta(self,*contas:Contas) -> list:
        self.valores_contas.extend(contas)
        return self.valores_contas
    
    def __repr__(self):
        class_name = type(self).__name__
        atrrs = f"{self.nome}"
        return f"{class_name}{atrrs}"
    

class Banco:
    def __init__(self,nome_cliente:str,agencia_cliente:str,conta_cliente:Contas) -> None:
        
        self.dados = []
        self.cliente = []
        self.nome_cliente = nome_cliente
        self.agencia_cliente = agencia_cliente
        self.conta_cliente = conta_cliente

    def verificar_agencia(self):
        for conta in self.dados:
            if self.agencia_cliente in conta.agencia:
                print(f"Esta aegncia {self.agencia_cliente} faz parte do banco")
            else:
                print(f"Esta agencia nao faz parte desse banco")

    def verificar_cliente(self):
        for cliente in self.cliente:
            if cliente.nome == self.nome_cliente:
                print(f"Este cliente {cliente.nome} e do banco")
            else:
                print(f"Este cliente {cliente.nome} nao e do banco")
    
    def verificar_conta_cliente(self):
        for conta in self.dados:
            if self.conta_cliente == conta.numero_conta  :
                print(f"Esta conta {self.conta_cliente} e do banco")
            else:
                print("Esta conta nao e do banco")
    
    def verificao_total(self) -> None:
        self.verificar_agencia()
        self.verificar_cliente()
        self.verificar_conta_cliente()


if __name__ == "__main__":
    c1 = Cliente("lucas",18)
    c2 = Cliente("joao",20)
    conta_cliente = ContaCorrente()
    conta_cliente.deposito(200)
    conta_cliente.sacar(201)
    conta_cliente.verificar_valor_extra()
    print(conta_cliente.saldo)
    conta_cliente2 = ContaPoupanca()
    c1.inserir_conta(conta_cliente)
    banco = Banco(c1.nome,conta_cliente.agencia,conta_cliente.numero_conta)
    banco.dados.extend([conta_cliente])
    banco.cliente.extend([c1,c2])
    banco.verificao_total()
