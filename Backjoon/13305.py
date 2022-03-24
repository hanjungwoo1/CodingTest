n = int(input())

roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = roads[0] * costs[0]
m = costs[0]
for i in range(1, n-1):

    m = min(costs[:i+1])
    print(costs[:i+1])
    print(m)
    result += roads[i] * m

print(result)

# n = int(input())
#
# roads = list(map(int, input().split()))
# costs = list(map(int, input().split()))
# res = 0
# m = costs[0]
#
# for i in range(n-1):
#     if costs[i] < m :
#         m = costs[i]
#
#     res += m* roads[i]
#
# print(res)