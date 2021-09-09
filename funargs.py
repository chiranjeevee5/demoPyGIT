"""position"""

def pos(name,age):
    print(name)
    print(age)


pos("Chiran",37)


"""Keyword"""

def pos2(name,age):
    print(name)
    print(age)

print("=================================")
pos2(age = 37, name = "Chiran")


"""Default"""

def pos1(name,age=18):
    print(name)
    print(age)

print("=================================")
pos1(name="Chiran")
pos1('Chiran')
pos1('Chiran' , 28)

"""Variable Length"""

def post1(a, *b):
    c = a

    for i in b:
        c= c+i
    print(c)

print("=================================")
post1(5,10,20,30,50)