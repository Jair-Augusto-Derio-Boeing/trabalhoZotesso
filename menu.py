from estudantes import createStudent, listStudent, editStudent, deleteStudent
from professor import createProfessor, listProfessor, editProfessor, deleteProfessor
from course import createCourse, listCourse, editCourse, deleteCourse 
from login import login

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Criar Estudante")
        print("2 - Criar Professor")
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

def menuProfessor(current_professor):
    while True:
        print("\n--- MENU PROFESSOR ---")
        print("1 - Criar novo estudante")
        print("2 - Listar estudantes")
        print("3 - Editar estudante")
        print("4 - Deletar estudante")
        print("5 - Criar novo professor")
        print("6 - Listar professores")
        print("7 - Editar professor")
        print("8 - Deletar professor")
        print("9 - Criar novo Curso")
        print("10 - Listar Cursos")
        print("11 - Editar Cursos")
        print("12 - Deletar Cursos")
        print("0 - Sair \n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            createStudent()
        elif opcao == "2":
            listStudent()
        elif opcao == "3":
            editStudent()
        elif opcao == "4":
            deleteStudent
        elif opcao == "5":
            createProfessor()
        elif opcao == "6":
            listProfessor()
        elif opcao == "7":
            editProfessor()
        elif opcao == "8":
            deleteProfessor()
        elif opcao == "9":
            createCourse(current_professor)
        elif opcao == "10":
            listCourse()
        elif opcao == "11":
            editCourse()
        elif opcao == "12":
            deleteCourse()
        elif opcao == "0":
            print("Saindo do menu do professor...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menuStudent():
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