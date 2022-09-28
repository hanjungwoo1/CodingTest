"""
입력

260000
4
20000 5
30000 2
10000 6
5000 8
"""

total_money = int(input())
count = int(input())

for _ in range(count):
    cost, ea = map(int, input().split())
    total_money -= cost * ea

if total_money == 0:
    print("Yes")
else:
    print("No")