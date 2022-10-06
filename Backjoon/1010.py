# import math
#
# m, n = map(int, input().split())
# result = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
#
# answer = 0
# for string in str(result)[::-1]:
#     if string == '0':
#         answer+=1
#     else:
#         break
#
# print(answer)


def countNum(N, num):
    count = 0
    divNum = num
    while( N >= divNum):
        count = count + (N // divNum)
        divNum = divNum * num
    return count

M, N = map(int, input().split())

print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))
