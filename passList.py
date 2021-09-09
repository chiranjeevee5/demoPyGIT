lst = []

a = int(input("Enter the value to be stored in the list - "))

for i in range(a):
    b = int(input("Enter the number - "))
    lst.append(b)

print(lst)

def count(lst):
    even = 0
    odd = 0
    
    for i in lst:
        if i%2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even , odd

e ,o = count(lst)

print (e)
print (o)

print("Even : {}, Odd : {}".format(e,o))