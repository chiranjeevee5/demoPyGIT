class car():
    wheels = 5

    def __init__(self):
        self.door = 2
        self.model = "Tesla"
        self.engine = "Automatic"


c1 = car()
c1.model = "BMW"
car.wheels = 4

c2 = car()
c2.door = 4
print(c1.door, c1.model, c1.engine, c1.wheels)
print(c2.door, c2.model, c2.engine,c2.wheels)