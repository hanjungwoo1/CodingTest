import sys
input = sys.stdin.readline

while True:
    length_edge= list(map(int, input().split()))
    length_edge.sort()

    if length_edge[0] == 0 & length_edge[1] == 0 & length_edge[2] == 0 :
        break

    if length_edge[0]*length_edge[0] + length_edge[1]*length_edge[1] == length_edge[2]*length_edge[2]:
        print("right")
    else:
        print("wrong")