# n = int(input())
#
# dp = []
# for _ in range(n):
#     data = list(map(int, input().split()))
#     dp.append(data)
#
# data = [[0] * i for i in range(1, n+1)]
# data[0] = dp[0]
# for i in range(n):
#     for x in range(i+1):
#         if x == 0:
#             data[i][x] = data[i-1][x] + dp[i][x]
#         elif x == i:
#             data[i][x] = data[i-1][x-1] + dp[i][x]
#         else:
#             data[i][x] = max(data[i-1][x-1], data[i-1][x]) + dp[i][x]
#
# print(max(data[n-1]))



n=int(input())
d=[]
for i in range(n):
  d.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(d[i])):
    if j==0:
      d[i][j]=d[i][j]+d[i-1][j]
    elif j==len(d[i])-1:
      d[i][j]=d[i][j]+d[i-1][j-1]
    else:
      d[i][j]=max(d[i-1][j-1],d[i-1][j])+d[i][j]
print(max(d[n-1]))
