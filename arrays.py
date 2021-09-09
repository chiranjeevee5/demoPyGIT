from array import *

"""vals = array('i',[5,9,8,4,2])
vals.reverse()
print(vals)

for i in range(5):
    print(vals[i])

print()
for i in range(len(vals)):
    print(vals[i])

print()

for e in vals:
    print(e)"""


vals = array('i',[5,9,8,4,2])
newArray = array(vals.typecode,(a*a for a in vals))

"""
for e in newArray:
    print(e)
"""

i=0
  
while i<len(newArray):
    print(newArray[i])
    i=i+1