pos = 0

def search(list, m):
    l = 0
    u = len(list)

    while l<=u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1


list = [1,3,5,7,9,10,400,540,987]
n = int(input("Enter the number for Binary Search : "))


if search(list , n):
    print("Value match found @ ", pos+1)
else:
    print("Value not found")