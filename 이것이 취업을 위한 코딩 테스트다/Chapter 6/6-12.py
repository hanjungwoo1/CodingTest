"""
입력 예시
5 3
1 2 4 5 3
5 5 6 6 5

출력 예시
26
"""

n, k = map(int, input().split())    # N과 K를 입력받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:   # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))  # 배열 A의 모든 원소 출력