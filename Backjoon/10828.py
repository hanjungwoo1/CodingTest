import sys


n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    data = sys.stdin.readline().split()

    if data[0] == 'push':
        arr.append(data[1])

    if data[0] == 'top':
        if len(arr) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(arr[-1]) + '\n')

    if data[0] == 'size':
        sys.stdout.write(str(len(arr)) + '\n')
    if data[0] == 'empty':
        if len(arr) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

    if data[0] == 'pop':

        if len(arr) > 0:
            sys.stdout.write(str(arr[-1]) + '\n')
            del arr[-1]
        else:
            sys.stdout.write(str(-1) + '\n')