n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            temp.pop()

dfs()