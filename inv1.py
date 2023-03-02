def find_inv(p):
    n = len(p)
    inv = [0 for x in range(n)]
    for k in range(n):
        for j in range(k, n):
            if p[k] > p[j]:
                inv[k] += 1
    return inv


p1 = [4, 3, 2, 5, 1, 6]
p2 = [3, 4, 5, 1, 2, 6]

print("The inversion sequence of ", p1, "is: ")
print(find_inv(p1))
print(" ")

print("The inversion sequence of ", p2, "is: ")
print(find_inv(p2))
