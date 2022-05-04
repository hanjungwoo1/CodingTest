"""
입력 1
"A man, a plan, a canal: Panama"
출력 1
true

입력 2
"race a car"
출력
false
"""

data = input()

strs = []

for i in data:
    if i.isalnum():
        strs.append(i.lower())

length = len(strs) // 2 + 1

for i in range(length):
    if strs[i] != strs[-(i+1)]:
        print(False)

print(True)