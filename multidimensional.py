from numpy import *
from numpy import matrix

arr1 = array([
                [1,2, 3, 4, 5, 6],
                [4,5,6,7,8,9]
            ])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()
print(arr2)

arr3 = arr2.reshape(2,2,3)
print(arr3)

m = matrix(arr1)
print(m)

m1 = matrix('1,2,3,4 ; 5,6,7,8')
print(m1)

print(m1.max())