
def home(k : int, n : int)-> int:
    if k==0:
        return n
    people = 0
    for j in range(1, n+1):
        people += home(k-1, j)
    return people

N = int(input())

for _ in range(N):
    stair = int(input())
    room_number = int(input())

    print(home(stair, room_number))