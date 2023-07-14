class Cliente:
    def __init__(self):
        self.nome = ""
        self.matricula = ""
    
    def cadastrar_cliente(self):
        self.nome = input("Digite o nome do cliente: ")
        self.matricula = int(input("Digite o número da matrícula: "))
    
    def mostrar_cliente(self):
        print("Nome:", self.nome)
        print("Matrícula:", self.matricula)
        
listaDeClientes = []
        
class Livro:
    def __init__(self):
        self.id = 0
        self.titulo = ""
        self.genero = ""
        self.autor = ""
        self.estoque = 0
    
    def cadastrar_livro(self):
        self.id = int(input("Informe um ID para o livro: "))
        self.titulo = input("Informe o título do livro: ")
        self.genero = input("Informe o gênero do livro: ")
        self.autor = input("Informe o autor do livro: ")
        self.estoque = int(input("Informe a quantidade em estoque do livro: "))

    def mostrar_livro(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Gênero:", self.genero)
        print("Autor:", self.autor)
        print("Quantidade em estoque:", self.estoque)

def buscar_livro():
    ID = int(input("Informe o ID do livro: "))
    for livro in listaDeLivros:
        if ID == livro.id:
            print("\nEsse ID corresponde ao livro", livro.titulo, "\n")
            livro.mostrar_livro()
            break
    else:
        print("\nID não encontrado, tente novamente\n")

def realizar_emprestimo():
    ID = int(input("Informe o ID do livro: "))
    for livro in listaDeLivros:
        if ID == livro.id:
            if livro.estoque > 0:
                livro.estoque -= 1
                print("Empréstimo realizado com sucesso!")
            else:
                print("Não há estoque disponível para este livro.")
            break
    else:
        print("Livro não encontrado.")

listaDeLivros = []

def menu():
    while True:
        opcao = int(input("1 - Cadastrar Novo Cliente\n2 - Mostrar Clientes\n3 - Cadastrar Novo Livro\n4 - Mostrar Livro\n5 - Buscar Livro por ID\n6 - Empréstimo\n7 - Sair\n"))
        
        if opcao == 1:
            cliente = Cliente()
            cliente.cadastrar_cliente()
            listaDeClientes.append(cliente)
        elif opcao == 2:
            for cliente in listaDeClientes:
                print("-------")
                cliente.mostrar_cliente()
        elif opcao == 3:
            livro = Livro()
            livro.cadastrar_livro()
            listaDeLivros.append(livro)
        elif opcao == 4:
            for livro in listaDeLivros:
                print("-------")
                livro.mostrar_livro()
        elif opcao == 5:
            print("\nBuscar Livro!")
            buscar_livro()
        elif opcao == 6:
            print("\nRealizar Empréstimo!")
            realizar_emprestimo()
        elif opcao == 7:
            print("\nSistema encerrado")
            break  
        else:
            print("Opção não encontrada, tente novamente")

menu()
