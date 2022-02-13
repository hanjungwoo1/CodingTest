n, m = map(int, input().split())


data = list(map(int, input().split()))
data.sort()

s = []
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in data:
    if i not in s:
      s.append(i)
      f()
      s.pop()

f()