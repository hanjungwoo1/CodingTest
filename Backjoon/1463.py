x = int(input())

d = [0] * (x+1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[x])




# ## 구현 파트, if들 진짜 어렵거나 // 진짜 문제를 쉽게 줬거나
# count = 0
# while x>1:
#     if x % 3 == 0 :
#         x = x/3
#         count += 1
#     elif x % 2 == 0:
#         x = x/2
#         count += 1
#     else:
#         x = x-1
#         count += 1
#     print(count, x)
# print(count)
