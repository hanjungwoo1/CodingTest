import math, sys

input = sys.stdin.readline

N = int(input())

result = math.factorial(N)

#print(result)

answer = 0
for x in str(result)[::-1]:
    if x == '0':
        answer += 1
    else:
        break

print(answer)
