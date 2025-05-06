from peewee import *

myDb = SqliteDatabase('dados.db')

class BaseModel(Model):
    class Meta:
        database = myDb

class Person(BaseModel):
    name = CharField()
    phone = CharField()
    email = CharField()
    password = CharField()

class Student(Person):
    ra = CharField()

class Professor(Person):
    siape = CharField()

class Course(BaseModel):
    professor = ForeignKeyField(Professor, backref='courses')
    discipline = CharField()
    title = CharField()
    description = TextField()
    content = TextField()

class Enrollment(BaseModel):
    student = ForeignKeyField(Student, backref='enrollments')
    course = ForeignKeyField(Course, backref='enrollments')

myDb.connect()
myDb.create_tables([Person, Student, Professor, Course, Enrollment])




