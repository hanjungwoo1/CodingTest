from collections import defaultdict

J = "aA"
S = "aAAbbbb"

dict = defaultdict(int)
result = 0

for x in S:
    dict[x] +=1

for y in J:
    result += dict[y]

print(result)