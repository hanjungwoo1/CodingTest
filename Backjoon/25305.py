def sol(nums, k):
    nums.sort(reverse=True)
    print(nums[k - 1])


n, k = map(int, input().split())
nums = list(map(int, input().split()))
sol(nums, k)