listaProfessores = []
listaCursos = []

class Professor():
    def __init__ (self):
        self.id = 0
        self.nome = ""
        self.formacao = ""
   
    def cadatrar_professor(self):
        self.id = int(input("ID: "))
        self.nome = input("Nome: ")
        self.formacao = input("Formação: ")
        return self
   
    def mostrar_professor(self):
        print("ID: ", self.id)
        print("Nome: ", self.nome)
        print("Formação: ", self.formacao)
    
    def buscar_professor(id):
        for professor in listaProfessores:
            if professor.id == id:
                return professor
            return print ("Professor não encontrado")
    
def menu_professor():
    while True:
        menu = int(input("\n1-Cadastrar Professor\n2-Professores cadastrados\n3-Sair\n"))
        match menu:
            case 1: 
                print("\nCADASTRO DE PROFESSOR\n")
                a = Professor()
                listaProfessores.append(a.cadatrar_professor())
            case 2: 
                print("\nPROFESSORES CADASTRADOS\n")
                for professor in listaProfessores:
                    print()
                    professor.mostrar_professor()
            case 3:
                print("Menu Professor Encerrado!")
                break
                
class Cursos():
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.descricao = ""
        self.cargaHoraria = 0
        self.professor = Professor()
        
    def cadastrar_curso(self, listaProfessores):
        self.id = int(input("ID: "))
        self.nome = input("Nome: ")
        self.descricao = input("Descricao do curso: ")
        self.cargaHoraria = int(input("Carga horária: "))
        while True:
            idProfessor = int(input("ID do Professor: (0 para ver lista de Professores)"))
            if idProfessor == 0:
                for professor in listaProfessores:
                    print()
                    professor.mostrar_professor()
            else:
                print("Professor selecionado: ", Professor.buscar_professor(idProfessor).nome)
                flag = int(input("Confirmar professor? 1- Sim e 2- Não"))
                if(flag == 1):
                    self.professor = Professor.buscar_professor(idProfessor)
                    break
    
    def mostrar_curso(self):
        print("ID: ", self.id)
        print("Nome: ", self.nome)
        print("Descrição do Curso: ", self.descricao)
        print("Carga Horária: ", self.cargaHoraria, " Horas")
        print("Professor: ", self.professor)
    
    def buscar_cursor(id):
        for curso in listaCursos:
            if curso.id == id:
                return curso
        return None
    
def menu_curso():
    while True:
        menu = int(input("\n1-Cadastrar Curso\n2-Cursos cadastrados\n3-Sair\n"))
        match menu:
            case 1: 
                print("\nCADASTRO DE CURSOS\n")
                b = Cursos()
                listaCursos.append(b.cadastrar_curso(listaProfessores))
            case 2: 
                print("\nCURSOS CADASTRADOS\n")
                for curso in listaCursos:
                    print()
                    curso.mostrar_curso()
            case 3:
                print("Menu Cursos Encerrado!")
                break
                
def menu_adm():
    while True:
        menu = int(input("\n1-Professores\n2-Cursos\n3-Sair\n"))
        match menu:
            case 1:
                print("\nMENU PROFESSOR\n")
                menu_professor()
            case 2:
                print("\nMENU CURSO\n")
                menu_curso()
            case 3:
                print("Sistema Encerrado.")
                break
menu_adm()
