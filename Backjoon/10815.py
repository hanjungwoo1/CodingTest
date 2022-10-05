N = int(input())

pocket_card = list(map(int, input().split()))

M = int(input())
check_card = list(map(int, input().split()))

# print(N, M)
# print(pocket_card)
# print(check_card)

pocket_card.sort()

def binary_search(array:list, target:int, start:int, end:int) -> bool:
    while start <= end:
        mid = (start+end) //2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for pop_card in check_card:
    if binary_search(pocket_card, pop_card, 0, N-1):
        print("1", end=" ")
    else:
        print("0", end=" ")