first = ["ccccc","b","aaaa","dd","eee"]
second = ["ff","hhhhh","ggg","jjjj","i"]
i = 0
l = 0
for x, y in enumerate(first):
    if len(y) > i:
        i = len(y)
        l = x
i2 = 0
l2 = 0
for x, y in enumerate(second):
    if len(y) > i2:
        i2 = len(y)
        l2 = x
second.append(first[l])
first.append(second[l2])
first.pop(l)
second.pop(l2)
print("first:", end=" ")
[print(x, end= " ") for x in first]
print()
print("second:", end=" ")
[print(x, end= " ") for x in second]
print()