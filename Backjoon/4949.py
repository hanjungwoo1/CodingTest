import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()

    data = []
    flag = "yes"
    for x in string:
        if x == '(' or x == '[':
            data.append(x)

        elif x == ']':
            if data and data[-1] == '[':
                data.pop()
            else:
                flag = "no"
                break

        elif x == ')':
            if data and data[-1] == '(':
                data.pop()
            else:
                flag = "no"
                break

        if x == '.':
            break

    if data:
        flag = "no"
    print(flag)

##################################################################################################################

# import sys
#
# input = sys.stdin.readline
#
# while 1:
#     string = input().rstrip()
#     stack = []
#     true_flag = 1
#
#     for cha in string:
#         if cha == '(' or cha == '[':
#             stack.append(cha)
#         elif cha == ')':
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#         elif cha == ']':
#             if stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 true_flag = 0
#                 break
#
#     if string == '.':
#         break
#
#     print("yes" if true_flag and not stack else "no")
