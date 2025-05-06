from classes import Student, Professor

def login():
    from menu import menuStudent, menuProfessor

    raSiapeLogin = input("RA ou SIAPE: ")
    passwordLogin = input("Senha: ")

    student = Student.select().where((Student.ra == raSiapeLogin) &
        (Student.password == passwordLogin)).first()
    if student:
        print("\nLogin como estudante realizado com sucesso.")
        menuStudent()
        return
    professor = Professor.select().where((Professor.siape == raSiapeLogin) &
        (Professor.password == passwordLogin)).first()

    if professor:
        print("\n Login como professor realizado com sucesso.")
        menuProfessor(professor)
    else:
        print("\n Usuário não existente")
