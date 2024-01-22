A_size = [4, 3, 2, 1, 5]
B_direction = [0, 1, 0, 0, 0]
surivovrs = len(A_size)
downstream = []
if not len(A_size):
        print("Survivors: " + str(surivovrs))
        exit()
for x in range(0, len(A_size)):
    print(A_size[x])
    if B_direction[x] == 1:
        downstream.append(A_size[x])
    else:
        while len(downstream):
            print(A_size[x] < downstream[-1])
            if A_size[x] < downstream[-1]: 
                surivovrs -= 1
                break
            else: 
                surivovrs -= 1
                downstream.pop()
    print(downstream)
print("Survivors: " + str(surivovrs))