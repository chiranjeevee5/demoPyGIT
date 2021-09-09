class methoddecl:
    Office ="World Bank"

    def __init__(self,m1,m2,m3,m4,m5):
        self.m1 = m1
        self.m2 = m1
        self.m3 = m1
        self.m4 = m1
        self.m5 = m1

    def avg(self):
        return(self.m1+self.m2+self.m3+self.m4+self.m5)/5

    @staticmethod
    def sm():
        print("Thanks for Reaching")

    @classmethod
    def cm(self):
        return(methoddecl.Office)


m1 =methoddecl(35,35,35,35,35)
m2 = methoddecl(40,40,40,40,40)

print("Person office is ", methoddecl.cm())
print("1 st Student Avg is " , m1.avg())
print("2 nd Student Avg is " , m2.avg())
m1.sm()