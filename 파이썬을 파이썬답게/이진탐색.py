import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
print(bisect.bisect(mylist, 11))
print(bisect.bisect(mylist, 10))
print(bisect.bisect(mylist, 8))