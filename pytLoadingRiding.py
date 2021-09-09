#Method OverLoading
class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calc(self, a = None, b= None, c= None):
        s = 0
        if a!= None and b!=None and c!=None:
            s = a+b+c
        elif a!= None and b!=None:
            s = a+b
        else:
            s =a
        return s

a1 = A(10,20)
print(a1.calc(120,36))


#Method Overriding
class B:
    def show(self):
        print("In B Show")

class C:
    def show(self):
        print("In C Show")

b = C()
b.show()