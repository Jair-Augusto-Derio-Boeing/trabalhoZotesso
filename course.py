from classes import Course

def createCourse(current_professor):

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

def editCourse():
    courseTitle = input("Informe o Título do curso que será editado: ")
    try:
        course = Course.get(Course.title == courseTitle)
        
        print(f"Editando curso: {course.title} ({course.discipline})")
        
        course.title = input(f"Título ({course.title}): ") or course.title
        course.discipline = input(f"Disciplina ({course.discipline}): ") or course.discipline
        course.description = input(f"Descrição ({course.description}): ") or course.description
        course.content = input(f"Conteúdo ({course.content}): ") or course.content
        
        course.save()
        
        print(f"\nCurso '{course.title}' editado com sucesso!\n")

    except Course.DoesNotExist:
        print("Curso não encontrado!")


def deleteCourse():
    courseTitle = input("Informe o Título do curso que será deletado: ")
    try:
        course = Course.get(Course.title == courseTitle)
        
        course.delete_instance()
        
        print(f"Curso '{course.title}' deletado com sucesso!\n")
    
    except Course.DoesNotExist:
        print("Curso não encontrado!")