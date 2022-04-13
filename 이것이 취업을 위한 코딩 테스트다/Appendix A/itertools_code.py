from itertools_code import combinations_with_replacement, combinations, permutations, product

data = ['A', 'B', 'C']


print(list(combinations(data, 2)))
print(list(permutations(data, 2)))
print(list(product(data, repeat = 2)))
print(list(combinations_with_replacement(data, 2)))