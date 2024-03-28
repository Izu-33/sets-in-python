set1 = set()
names = ['Onyinye', 'Kunle', 'Bolowei', 'Peter']
set1.update(names)
print(set1)

set2 = set()
nums = [1, 2, 3, 4]
set2.update(nums)
print(set2)

set3 = set1.union(set2)
set4 = set2.union(set1)

print(set3)
print(set4)

set5 = set1 | set2
print(set5)