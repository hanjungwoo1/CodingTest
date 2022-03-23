"""
5
3 2 1 1 9
"""


n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    print(target, x)
    if target < x:
        break
    target += x
    print(target)

# 만들 수 없는 금액 출력
print(target)