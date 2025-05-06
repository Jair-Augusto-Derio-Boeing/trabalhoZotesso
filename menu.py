from classes import Student, Professor, Course

current_professor = None


def createPerson():
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    password = input("Senha: ")

    person = {
        "name": name,
        "phone": phone,
        "email": email,
        "password": password
    }

    return person


def createStudent():
    person = createPerson()
    ra = input("Matrícula: ")

    student = Student.create(
        name=person["name"],
        phone=person["phone"],
        email=person["email"],
        password=person["password"],
        ra=ra
    )
    print(f"\nEstudante {person['name']} criado com sucesso!\n")


def listStudent():
    lista = Student.select()

    print("\n-------- Lista de Estudantes --------")
    print("Total de estudantes:", len(lista), "\n")

    for student in lista:
        print(f"Nome: {student.name} ({student.ra})")


def createProfessor():
    person = createPerson()
    siape = input("SIAPE: ")

    professor = Professor.create(
        name=person["name"],
        phone=person["phone"],
        email=person["email"],
        password=person["password"],
        siape=siape
    )
    print(f"\nProfessor {person['name']} criado com sucesso!\n")


def listProfessor():
    lista = Professor.select()

    print("\n-------- Lista de Professores --------")
    print("Total de professores:", len(lista), "\n")

    for professor in lista:
        print(f"Nome: {professor.name} ({professor.siape})")


def login():
    global current_professor

    raSiapeLogin = input("RA ou SIAPE: ")
    passwordLogin = input("Senha: ")

    student = Student.select().where((Student.ra == raSiapeLogin) &
        (Student.password == passwordLogin)).first()
    professor = Professor.select().where((Professor.siape == raSiapeLogin) &
        (Professor.password == passwordLogin)).first()

    print("\n")

    if student:
        print("Login como estudante realizado com sucesso.")
        menuAluno()
    elif professor:
        print("Login como professor realizado com sucesso.")
        current_professor = professor
        menuProfessor()
    else:
        print("Usuário não existente")


def createCourse():
    global current_professor

    if current_professor is None:
        print("Erro: Nenhum professor logado.")
        return

    title = input("Título: ")
    discipline = input("Disciplina: ")
    description = input("Descrição: ")
    content = input("Conteúdo: ")

    course = Course.create(
        professor=current_professor,
        title=title,
        discipline=discipline,
        description=description,
        content=content
    )

    print(f"\nCurso '{course.title}' criado com sucesso!\n")

def listCourse():
    lista = Course.select()

    print("\n-------- Lista de Cursos --------")
    print("Total de Cursos:", len(lista), "\n")

    for course in lista:
        print(f"Nome: {course.title} ({course.discipline})")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Criar novo estudante")
        print("2 - Criar novo professor")
        print("3 - Login")
        print("0 - Sair \n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            createStudent()
        elif opcao == "2":
            createProfessor()
        elif opcao == "3":
            login()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menuProfessor():
    while True:
        print("\n--- MENU PROFESSOR ---")
        print("1 - Criar novo estudante")
        print("2 - Listar estudantes")
        print("3 - Criar novo professor")
        print("4 - Listar professores")
        print("5 - Criar novo Curso")
        print("6 - Listar Cursos")
        print("0 - Sair \n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            createStudent()
        elif opcao == "2":
            listStudent()
        elif opcao == "3":
            createProfessor()
        elif opcao == "4":
            listProfessor()
        elif opcao == "5":
            createCourse()
        elif opcao == "6":
            listCourse()
        elif opcao == "0":
            print("Saindo do menu do professor...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menuAluno():
    while True:
        print("\n--- MENU ALUNO ---")
        print("1 - Listar professores")
        print("2 - Listar Cursos")
        print("0 - Sair \n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listProfessor()
        elif opcao == "2":
            listCourse()
        elif opcao == "0":
            print("Saindo do menu do aluno...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
