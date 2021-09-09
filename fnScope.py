a = 10
print(id(a))

def something():
    """global a"""
    a= 9
    x=globals()['a']
    print(id(x))
    print('in fun', a)
    globals()['a'] = 15

something()

print('out fun' , a)