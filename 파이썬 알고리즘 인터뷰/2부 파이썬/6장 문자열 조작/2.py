""""
입력 1
["h", "e", "l", "l", "o"] // hello
출력 1
["o", "l", "l", "e", "h"]

입력 2
["H", "a", "n", "n", "a", "h"] // Hannah
출력 2
["h", "a", "n", "n", "a", "H"]
"""

data = list(input())
print(data)
data = data[::-1]
print(data)