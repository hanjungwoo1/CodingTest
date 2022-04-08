"""
입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력 예시
19
16
"""

for tc in range(int(input())):

    n, m = map(int, input().split())
    array = list(map(int, input().split()))


    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    #print(dp)

    for y in range(1, m):
        for x in range(n):
            #print(x, y)
            if x == 0:
                dp[x][y] = dp[x][y] + max(dp[x][y-1], dp[x+1][y-1])
            elif x == (n-1):
                dp[x][y] = dp[x][y] + max(dp[x-1][y-1], dp[x][y-1])
            else:
                dp[x][y] = dp[x][y] + max(dp[x-1][y-1], dp[x][y-1], dp[x+1][y-1])

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)