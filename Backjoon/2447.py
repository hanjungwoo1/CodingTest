# 별들을 만들 함수
def get_stars(n):
    # 별들을 담을 리스트
    Temp = []
    #
    for i in range(3 * len(n)):
        # n(즉 len(stars))이 3으로 나누어 떨어지지 않는다면(1이 남는다면) 가운데 공백을 줌(n의 길이 만큼)
        if i // len(n) == 1:
            Temp.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])

        # n이 3으로 나누어 떨어진다면, 공백 없이 가득 채움
        else:
            Temp.append(n[i % len(n)] * 3)

    return Temp


stars = ["***", "* *", "***"]
n = int(input())
k = 0

# 만약 n이 3이 될 때 까지 n은 3으로 나눠준 값을 다시 n값으로 지정하고 k 1씩 추가
while n != 3:
    n = int(n / 3)

    # k는 함수를 몇번 실행할지 정하는 변수
    k += 1

for i in range(k):
    stars = get_stars(stars)
for i in stars:
    print(i)