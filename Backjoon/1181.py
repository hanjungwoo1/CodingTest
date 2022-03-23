n = int(input())

dict = {}

for _ in range(n):
    data = input()
    dict[data] = len(data)

sorted_dict = sorted(dict.items(), key = lambda item : (item[1], item[0]))

for x,y in sorted_dict:
    print(x)