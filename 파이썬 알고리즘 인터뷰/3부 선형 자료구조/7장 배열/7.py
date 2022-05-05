nums = [2, 7, 11, 15]
target = 9

# first
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])


# second
for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i + 1:]:
        print([nums.index(n), nums[i + 1:].index(complement) + (i + 1)])
        print([nums.index(n), nums.index(complement)])