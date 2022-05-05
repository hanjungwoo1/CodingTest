from collections import defaultdict

paragraph = "Bot hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

my_dict = defaultdict(int)

for x in paragraph.lower().split():
    temp = ""

    for y in x:
        if y.isalnum():
            temp += y

    if temp not in banned:
        my_dict[temp] += 1
    else:
        print(temp, "banned")

print(my_dict)
print(max(my_dict, key=my_dict.get))