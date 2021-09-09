f = open("myData.txt",'r')

#print(f.readline(4),end="")


f2 = open("abcd.txt",'w')

for data in f:
    f2.write(data)