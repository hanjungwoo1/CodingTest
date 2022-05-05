from collections import defaultdict

data = ["eat", "tea", "tan", "ate", "nat", "bat"]

data.sort()
print(data)

my_dict = defaultdict(list)

for x in data:
    my_dict[''.join(sorted(x))].append(x)

print(my_dict)

result = list(my_dict.values())
print(result)