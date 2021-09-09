#With Single Number addition
class A():
	def __init__(self,a):
		self.a = a

	def __add__(self, other):
		return self.a + other.a

a1 = A(2)
a2 = A(3)

print(a1+a2)


# With Two numbers addition
class B:
	def __init__(self,b,c):
		self.b = b
		self.c = c

	def __add__(self, other):
		#return self.b+other.b,self.b+other.c
		return '{},{}'.format(self.b + self.c, other.b + other.c)

b1 = B(2,6)
b2 = B(5,7)

print(b1+b2)

#Greater than
class C():
	def __init__(self,c):
		self.c = c
	def __gt__(self, other):
		if(self.c>other.c):
			return True
		else:
			return False

c1 = C(2)
c2 = C(5)

if(c1>c2):
	print("C1 is Greater")
else:
	print("C2 is Greater")

# Lesser than or Equal to
class A:
	def __init__(self, a):
		self.a = a

	def __lt__(self, other):
		if (self.a < other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"

	def __eq__(self, other):
		if (self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)


# Operator Overloading
class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __add__(self, other):
		x = self.x+self.y
		y = other.y+other.y
		return Point(x,y)

	def __str__(self):
		return '{},{}'.format(self.x,self.y)

p1 = Point(3,5)
p2 = Point(10, 40)

print(p1+p2)