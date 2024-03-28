set1 = set([1, 3, 5, 7])
set2 = set([2, 3, 4, 5])

set3 = set1.difference(set2)
print(set3)

set4 = set2.difference(set1)
print(set4)

set5 = set1 - set2
print(set5)