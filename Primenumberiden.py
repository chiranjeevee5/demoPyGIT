"""num = int(input("Enter the number - "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break"""

prime =[]
for i in range(1,101):
    x=2
    y=0
    while x<=i:
        if i%x==0:
            y+=1
        x+=1
    if y<=1:
        if i==1:
            continue
        else:
            prime.append(i)
print(prime)