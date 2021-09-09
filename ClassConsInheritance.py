class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 - A is Working")

    def feature2(self):
        print("Feature 2 is Working")

# class B(A):
class B:
    def __init__(self):
        #super(B, self).__init__()
        print("in B init")

    def feature3(self):
        print("Feature 1 - B is Working")

    def feature4(self):
        print("Feature 4 is Working")

#a = B()
#a.feature3()

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def fea(self):
        super().feature3()

a = C()
a.fea()