A_size = [4, 3, 2, 1, 5]
B_direction = [0, 1, 0, 0, 0]
surivovrs = 0
downstream = []
for x in range(1, len(A_size)):
    if B_direction[x] == 1:
        downstream.append(A_size[x])
    else:
        if len(downstream) != 0:
            while len(downstream) != 0:
                if A_size[x] > downstream[-1]: break
                else: downstream.pop()
        else: surivovrs += 1
print("Survivors: " +str(surivovrs + len(downstream)))