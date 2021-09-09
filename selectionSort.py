
def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] <nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


nums = [3,6,5,1,4,8,10,2]

sort(nums)

print(nums)