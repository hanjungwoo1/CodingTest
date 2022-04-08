"""
입력 예시 1
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

출력 예시 1
45
"""

n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)



print(n)
print(t)
print(p)
print(dp)

for i in range(n-1, -1, -1):
    #print(i)
    time = t[i] + i

    if time <= n:
        #print(time, i)
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(dp)
print(max(dp))