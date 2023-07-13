class Cliente:
    def __init__(self, nome, cnpj, saldo):
        self.nome = nome
        self.cnpj = cnpj
        self.saldo = saldo

    def definir_nome(self, nome):
        self.nome = nome

    def obter_nome(self):
        return self.nome

    def definir_cnpj(self, cnpj):
        self.cnpj = cnpj

    def obter_cnpj(self):
        return self.cnpj

    def definir_saldo(self, saldo):
        self.saldo = saldo

    def obter_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso! Novo saldo:", self.saldo)
        
    def sacar (self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso! Novo saldo:", self.saldo)
        else:
            print("Saldo insuficiente, você tem disponível para saque: ", self.saldo)

clientes = []  



class Gerente:
    def __init__(self, nome, banco, cpf):
        self.nome = nome
        self.banco = banco
        self.cpf = cpf

    def definir_nome(self, nome):
        self.nome = nome

    def obter_nome(self):
        return self.nome

    def definir_banco(self, banco):
        self.banco = banco

    def obter_banco(self):
        return self.banco

    def definir_cpf(self, cpf):
        self.cpf = cpf

    def obter_cpf(self):
        return self.cpf

gerentes = []

while True:
    print("Menu de acesso:")
    print("1. Cadastrar cliente")
    print("2. Exibir clientes cadastrados")
    print("3. Efetuar depósito (Clientes)")
    print("4. Efetuar saque (Clientes)")  
    print("5. Consultar Saldo (Clientes)")  
    print("6. Cadastrar gerente")
    print("7. Exibir gerentes cadastrados")
    print("8. Sair do programa")

    menu = input("O que você deseja fazer?: ")

    if menu == "1":
        nome = input("Digite o nome do cliente: ")
        cnpj = input("Digite o CNPJ do cliente: ")
        saldo = float(input("Digite o saldo do cliente: "))

        cliente = Cliente(nome, cnpj, saldo)
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    elif menu == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            print("Clientes cadastrados:")
            for cliente in clientes:
                print("Nome:", cliente.obter_nome())
                print("CNPJ:", cliente.obter_cnpj())
                print("Saldo:", cliente.obter_saldo())

    elif menu == "3":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            nome_cliente = input("Digite o nome do cliente: ")
            valor_deposito = float(input("Digite o valor do depósito: "))

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.obter_nome() == nome_cliente:
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado is not None:
                cliente_encontrado.depositar(valor_deposito)
            else:
                print("Cliente não encontrado.")
            
    elif menu == "4":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            nome_cliente = input("Digite o nome do cliente: ")
            valor_saque = float(input("Digite o valor do saque: "))

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.obter_nome() == nome_cliente:
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado is not None:
                cliente_encontrado.sacar(valor_saque)
            else:
                print("Cliente não encontrado.")
                
    elif menu == "5":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            nome_cliente = input("Digite o nome do cliente: ")

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.obter_nome() == nome_cliente:
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado is not None:
                print("Saldo atual: ", cliente_encontrado.obter_saldo())
            else:
                print("Cliente não encontrado.")
                
    elif menu == "6":
        nome = input("Digite o nome do gerente: ")
        banco = input("Digite o banco do gerente: ")
        cpf = input("Digite o cpf do gerente: ")

        gerente = Gerente(nome, banco, cpf)
        gerentes.append(gerente)
        print("Gerente cadastrado com sucesso!")

    elif menu == "7":
        if len(gerentes) == 0:
            print("Nenhum gerente cadastrado.")
        else:
            print("Gerentes cadastrados:")
            for gerente in gerentes:
                print("Nome:", gerente.obter_nome())
                print("Banco:", gerente.obter_banco())
                print("CPF:", gerente.obter_cpf())

    elif menu == "8":
        print("Processo finalizado.")
        break

    else:
        print("Opção inválida. Selecione uma das opções do menu.")