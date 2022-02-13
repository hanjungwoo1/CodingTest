n, m = map(int, input().split())

s = []
def f(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(start, n + 1):

    s.append(i)
    f(i)
    s.pop()

f(1)