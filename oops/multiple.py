class Teacher:
    def teach(self):
        print("Teacher teaches students")

class Writer:
    def write(self):
        print("Writer writes books")

class Person(Teacher, Writer):
    def speak(self):
        print("Person speaks")

p = Person()
p.teach()
p.write()
p.speak()