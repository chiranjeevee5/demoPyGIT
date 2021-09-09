class innerclass:
    def __init__(self,name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.lap = self.subclass()

    def show(self):
        print('Name is - ',self.name, '\nAge is - ', self.age,'\nLocation is - ',self.location)
        self.lap.show()

    class subclass():
        def __init__(self):
            self.laptop = "Apple Laptop "
            self.Phone = 'iPhone Xs Max'
            self.watch = 'Apple Watch'

        def show(self):
            print("Uses - ", self.laptop, "; Speaks in - ", self.Phone, "; Utilize - ", self.watch)

s1 = innerclass('Chiranjeevee',37,'Washington DC')
s2 = innerclass('Deekshitha',27,'Washington DC')
s1.show()
print()
s2.show()