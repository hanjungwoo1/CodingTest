# data = input()
#
# dict = {}
# for x in data:
#     if x in dict:
#         dict[x] = dict[x]+1
#     else:
#         dict[x] = 1
#
# sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
# print(dict.items())
# print(sorted_dict)

inputData = input().upper()
searchKeys = list(set(inputData))

countArr = []
for key in searchKeys:
    countArr.append(inputData.count(key))

if countArr.count(max(countArr)) > 1:
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))])