"""def topten():
    yield 1

value = topten()

print(value.__next__())"""

def topten():
    n = 1
    while n<=10:    
        sq = n*n
        yield sq
        n += 1

val = topten()
for i in val:
    print(i)