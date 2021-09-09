#Single Inheritance
print()
print('Single Inheritance')
class A():
    def feature1(self):
        print("Feature 1 is Working")

    def feature2(self):
        print("Feature 2 is Working")

a = A()
a.feature1()
a.feature2()

#Multilevel Inheritance
print()
print('MultiLevel Inheritance')
class B(A):
    def feature3(self):
        print("Feature 3 is Working")

    def feature4(self):
        print("Feature 4 is Working")

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

#Multiple Inheritance
print()
print("Multiple Inheritance")

class C():
    def feature1(self):
        print("Feature 1 is Working")

    def feature2(self):
        print("Feature 2 is Working")

class D():
    def feature3(self):
        print("Feature 3 is Working")

    def feature4(self):
        print("Feature 4 is Working")

class E(C, D):
    def feature_Nth(self):
        print("Feature_Nth is Working")

e = E()
e.feature1()
e.feature2()
e.feature3()
e.feature4()
e.feature_Nth()