num_list = [3, 18, 78, 74, 50, 66, 20, 99, 100]
for x in range(len(num_list)):
    max = x
    for y in range(x+1, len(num_list)):
        if num_list[y] > num_list[max]:
            max = y
    temp = num_list[x]
    num_list[x] = num_list[max]
    num_list[max] = temp
print(num_list)
