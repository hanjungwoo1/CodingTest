import sys, math

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

for each_data in data[1:]:

    gcd = math.gcd(data[0], each_data)
    print(str(data[0]//gcd)+"/"+str(each_data//gcd))