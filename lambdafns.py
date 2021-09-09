from functools import reduce

"""def is_even(n):
    return n%2 == 0

nums = [3,6,5,4,3,5,7,8,9,20]

evenno = list(filter(is_even,nums))

print(evenno)"""

""" Filter - Lambada """

num=[2,4,3,5,7,6,8,0,10,23,34,45,67]

evens = list(filter(lambda n :n%2 == 0, num))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(lambda a,b : a+b,doubles)

print(evens)

print(doubles)

print(sum)