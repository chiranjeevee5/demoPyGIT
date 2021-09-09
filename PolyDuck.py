
class pycharm:
    def execute(self):
        print("Compile the Code")
        print("Run the Program")

class Eclipse:
    def execute(self):
        print("Spell Check")
        print("Assign Project")
        print("Compile the code")
        print("Run the program")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Eclipse()

lap1 = Laptop()
lap1.code(ide)


# Python program to demonstrate
# duck typing


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")


# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()