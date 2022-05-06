"""
입력
()[]{}

출력
true
"""
data = input()

stack = []

for x in data:
    if x == ')':
        if stack and stack.pop() == '(':
            continue

    if x == ']':
        if stack and stack.pop() == '[':
            continue

    if x == '}':
        if stack and stack.pop() == '{':
            continue

    stack.append(x)

if stack:
    print("false")
else:
    print("true")