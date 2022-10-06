import sys

input = sys.stdin.readline

N = int(input())

fib_count = 0
fibonacci_count = 0

def fib(n: int) -> int:
    global fib_count
    if n == 1 or n ==2 :
        fib_count += 1
        return 1;
    else:
        return (fib(n-1) + fib(n-2))

def fibonacci(n: int):
    global fibonacci_count

    fib_array = [0] * (n+1)
    fib_array[1] = 1
    fib_array[2] = 1

    for i in range(3,n+1):
        fibonacci_count += 1
        fib_array[i] = fib_array[i-1] + fib_array[i-2]

fib(N)
fibonacci(N)

print(fib_count, fibonacci_count)

