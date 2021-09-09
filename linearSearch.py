pos = 0

def search(list, n):
    i = 0

    while i< len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1;
    return False

list = [4,6,1,3,7,9,9]
n = int(input("Enter the value to search : "))

if search(list , n):
    print("Value found @ ", pos)
else:
    print("Value not found")