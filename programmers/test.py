a, b = map(int, input().split())

new_a = a
new_b = b - 45
if new_b < 0:
    new_a = a-1
    new_b = 60+new_b

if new_a < 0:
    new_a = 23

print(new_a, new_b, end='')