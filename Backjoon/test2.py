from collections import defaultdict

data = defaultdict(list)

data['사과'] = "Apple"
print(data)



list = defaultdict(list)
list[0].extend(data['사과'])
print(list)
list[0].extend([1,2,3])
print(list[0])