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
