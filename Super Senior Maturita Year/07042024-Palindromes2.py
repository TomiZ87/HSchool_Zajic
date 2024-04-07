a = [1, 2, 3, 2, 8]
b = a
result = True
if len(a) == len(b):
    for i in range(len(a)):
        if not (a[i] == b[-i - 1]):
            result = False
else:
    print("Not Equal")

print(result)
b = a.copy()
b.reverse()
print(a == b)
