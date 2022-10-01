count = int(input())


for _ in range(count):
    H, W, N = map(int, input().split())
    stage = N % H
    number = 1 + (N // H)

    if N % H == 0:
        number = N // H
        stage = H

    print(str(stage * 100 + number))