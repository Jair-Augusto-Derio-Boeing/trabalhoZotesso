from classes import Student
from person import createPerson

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
    print(f"\nEstudante {student.name} criado com sucesso!\n")

def listStudent():
    lista = Student.select()

    print("\n-------- Lista de Estudantes --------")
    print("Total de estudantes:", len(lista), "\n")

    for student in lista:
        print(f"Nome: {student.name} ({student.ra})")

def editStudent():
    ra = input("Informe a matrícula do estudante que será editado: ")
    try:
        student = Student.get(Student.ra == ra)
        student.name = input("Nome: ")
        student.phone = input("Telefone: ")
        student.email = input("Email: ")
        student.password = input("Senha: ")
        student.ra = input("Matrícula: ")
        student.save()

        print(f"\nEstudante {student.name} editado com sucesso!")
    except Student.DoesNotExist:
        print("Estudante não existe!")

def deleteStudent():
    ra = input("Informe a matrícula do estudante que será deletado: ")
    try:
        student = Student.get(Student.ra == ra)
        student.delete_instance()
        print(f"Estudante com matrícula {ra} deletado com sucesso!")
    except Student.DoesNotExist:
        print("Estudante não existe!")
