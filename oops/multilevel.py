class Person:
    def name(self):
        print("My name is Raju")

class Employee(Person):
    def job(self):
        print("I am an Employee")

class Manager(Employee):
    def manage(self):
        print("I manage the team")

m = Manager()
m.name()
m.job()
m.manage()