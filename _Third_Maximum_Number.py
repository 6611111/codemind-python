def thirdMax(nums):
    nums.sort(reverse = True)
    count = 1
    previous = nums[0]

    for i in range(len(nums)):
        if nums[i] != previous:
            count = count + 1
            previous = nums[i]
        if count == 3:
            return nums[i]
    return nums[0] 
n=int(input())
nums = list(map(int,input().split()))
print(thirdMax(nums))