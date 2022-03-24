n = int(input())

data = list(map(int, input().split()))
data.sort()
# 최소값을 필요로 하기에, 적은 수 부터 연산하는 것이 최소
total = 0
result = 0
for x in data:
    total = total + x
    result = total + result
print(result)