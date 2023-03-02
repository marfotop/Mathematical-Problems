import math as mt


def find_inv(p):
    n = len(p)
    inv = [0 for x in range(n)]
    for k in range(n):
        for j in range(k, n):
            if p[k] > p[j]:
                inv[k] += 1
    return inv


def find_rank(inv):
    n = len(inv)
    rank = 0
    j = 0
    for i in range(n-1, 0, -1):
        rank += (inv[j] * mt.factorial(i))
        j += 1
    return rank


p1 = [3, 1, 2, 4]
print("Permutation =", p1)
print("Inversion sequence =", find_inv(p1))
print("Rank =", find_rank(find_inv(p1)))
print(" ")

p2 = [3, 1, 5, 4, 2]
print("Permutation =", p2)
print("Inversion sequence =", find_inv(p2))
print("Rank =", find_rank(find_inv(p2)))
print(" ")

p3 = [4, 3, 2, 5, 1, 6]
print("Permutation =", p3)
print("Inversion sequence =", find_inv(p3))
print("Rank =", find_rank(find_inv(p3)))


