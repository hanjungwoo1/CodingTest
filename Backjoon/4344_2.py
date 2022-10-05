import sys

input = sys.stdin.readline


n = int(input())

# print(n)
# print(type(n))

for _ in range(5):
    problem_list = list(map(int, input().split()))

    total_sum = sum(problem_list[1:])
    avg = total_sum / problem_list[0]

    count = 0

    for x in problem_list[1:]:
        if x > avg:
            count += 1

    #print("%.3f" % avg)
    print("%.3f" % (count /problem_list[0] * 100) + '%')


