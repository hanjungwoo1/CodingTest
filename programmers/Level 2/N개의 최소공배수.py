def solution(arr):
    left = arr[0]

    for i in range(1, len(arr)):
        right = arr[i]

        print(left, right)
        x = left
        y = right
        while True:
            if x == y:
                left = x
                break

            elif x > y:
                y += right

            else:
                x += left

    return left