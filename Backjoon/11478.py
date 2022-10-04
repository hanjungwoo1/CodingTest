S = input()

ans = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        ans.add(temp)

print(len(ans))
