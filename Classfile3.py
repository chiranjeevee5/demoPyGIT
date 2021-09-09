class computer:
   def __init__(self):
       self.name = "Navin"
       self.age = 20


   def compare1(self, other):
       if self.age == other.age:
           return True
       else:
            return False


c1 = computer()
c1.age = 30
print(c1.name)
print(c1.age)


c2 = computer()
if c1.compare1(c2):
    print("Both are same")
else:
    print("Both are different")

print(c2.age)
