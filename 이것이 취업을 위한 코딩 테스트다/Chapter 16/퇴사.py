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

입력 예시 2
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

출력 예시 2
55

입력 예시 3
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

출력 예시 3
20

입력 예시 4
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

출력 예시 4
90
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

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)