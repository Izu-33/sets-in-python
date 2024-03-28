myset = set()
names = ['Onyinye', 'Kunle', 'Bolowei', 'Peter']
myset.update(names)
print(myset)

val = "Kunle" in myset
print(val)

name = "Kunle"

if name in myset:
    print(f"{name} is an element of the set")
else:
    print(f"{name} is not part of the set")