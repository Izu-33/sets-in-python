set1 = set([1, 2, 3, 4])
set2 = set([2, 3])

val = set2.issubset(set1)
print(val)

val2 = set1.issuperset(set2)
print(val2)

val3 = set2 <= set1
val4 = set1 >= set2
print(val3)
print(val4)