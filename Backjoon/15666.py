n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(start, n):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            temp.pop()

dfs(0)