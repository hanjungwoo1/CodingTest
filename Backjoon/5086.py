import sys

input = sys.stdin.readline

while True:
    first_number, second_number = map(int, input().split())

    if first_number == 0 and second_number == 0:
        break

    if second_number % first_number == 0 and first_number < second_number:
        print("factor")
    elif first_number % second_number == 0 and first_number > second_number:
        print("multiple")
    else:
        print("neither")