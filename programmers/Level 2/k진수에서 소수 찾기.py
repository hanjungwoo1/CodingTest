def to_k_number(n, k):  # n을 k진수로 반환
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n // k
    return ''.join(reversed(ret))


def is_prime_num(k):
    if k == 2 or k == 3: return True  # 2 or 3 은 소수
    if k % 2 == 0 or k < 2: return False  # 2의 배수이거나 2보다 작은 값인 경우 소수가 아님
    # 3부터 root(k)까지 2씩 증가하며 확인(3, 5, 7...),
    # 이는 작은 값들의 배수일 때 발생하는 중복을 제거하며 확인(소수 찾기 최적화)
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_num = to_k_number(n, k)  # k진수로 반환
    # k_num을 0을 기준으로 분할하여 n을 가져옴
    for n in k_num.split('0'):
        if n == "": continue
        if is_prime_num(int(n)):  # n이 소수인 경우 answer+=1
            answer += 1
    return answer
