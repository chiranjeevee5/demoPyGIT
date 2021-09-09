#nums = [1,2,3,4]
#it = iter(nums)
#print(next(it))

"""class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

vl = topten()
print(next(vl))

for i in vl:
    print(i)"""

class Test:
    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1;
        return x

# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothings
for i in Test(5):
    print(i)