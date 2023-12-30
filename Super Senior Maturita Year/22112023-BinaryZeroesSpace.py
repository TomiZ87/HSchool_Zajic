binary_zeroes = str(input("Please enter the binary: "))
binary = "01"
for x in binary_zeroes:
    if x not in binary:
        print(x)
        print("The number isnt binary")
        exit()
zeroes = 0
zeroes_array = []
binary_zeroes = int(binary_zeroes)
binary_zeroes = str(binary_zeroes)
for y in binary_zeroes:
    if y == "1":
        zeroes_array.append(zeroes)
        zeroes = 0
    if y == "0":
        zeroes += 1
print("The number has " +str(max(zeroes_array)) + " binary 0 spaces.")
    