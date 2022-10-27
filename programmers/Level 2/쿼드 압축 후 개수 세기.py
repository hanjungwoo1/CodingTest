def quard(x, y, n):
    first = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != first:
                n //= 2
                quard(x, y, n)
                quard(x, y + n, n)
                quard(x + n, y, n)
                quard(x + n, y + n, n)
                return

    answer[first] += 1