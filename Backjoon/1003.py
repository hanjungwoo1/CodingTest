# N = int(input())
# list = []
#
# for i in range(N):
#     list.append(int(input()))
#
# fibo = [[i, i] for i in range(max(list) +1)]
# #print(fibo)
#
#
# fibo[0] = [1, 0]
# fibo[1] = [0, 1]
#
# #print(N)
# #print(list)
#
#
# for i in range(2, max(list) +1) :
#     fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
#     fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]
#
# #print(fibo)
#
# for x in list:
#     print(fibo[x])


a = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]


def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[num], one[num]))


for i in range(a):
    k = int(input())
    cal(k)
