from array import *
from builtins import type, input

arr = array('i',[])
n = int(input("Enter the length of the Array "))

for i in range(n):
    x = int(input("Enter the Values in array "))
    arr.append(x)

for y in range(len(arr)):
    print(arr[y])

val = int(input("Enter the value for search "))

k=0
for z in arr:
    if z == val:
        print(k)
        break
    k+=1

print(arr.index(val))