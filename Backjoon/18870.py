import sys
n = int(sys.stdin.readline())

data =list(map(int, sys.stdin.readline().split()))

new_data = sorted(list(set(data)))

# for x in data:
#     print(new_data.index(x), end= " ")

dic = {new_data[i] : i for i in range(len(new_data))}
for x in data:
    print(dic[x], end= " ")