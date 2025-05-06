from classes import Professor
from person import createPerson

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
    print(f"\nProfessor {professor.name} criado com sucesso!\n")

def listProfessor():
    lista = Professor.select()

    print("\n-------- Lista de Professores --------")
    print("Total de professores:", len(lista), "\n")

    for professor in lista:
        print(f"Nome: {professor.name} ({professor.siape})")

def editProfessor():
    siape = input("Informe o siape do professor que será editado: ")
    try:
        professor = Professor.get(Professor.siape == siape)
        professor.name = input("Nome: ")
        professor.phone = input("Telefone: ")
        professor.email = input("Email: ")
        professor.password = input("Senha: ")
        professor.siape = input("SIAPE: ")
        professor.save()

        print(f" \n Professor {professor.name} editado com sucesso!")
    except Professor.DoesNotExist:
        print("Professor não existe!")

def deleteProfessor():
    siape = input("Informe o siape do professor que será deletado: ")
    try:
        professor = Professor.get(Professor.siape == siape)
        professor.delete_instance()
        print(f"Professor com SIAPE {siape} deletado com sucesso!")
    except Professor.DoesNotExist:
        print("Professor não existe!")
