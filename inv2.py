def find_per(s):
    n = len(s)
    per = [0 for x in range(n)]
    l = [0 for x in range(n)]
    for x in range(n):
        l[x] = x + 1
    # print(l)
    for x in range(n):
        for k in range(n):
            found = False
            cnt = -1
            for j in range(n):
                if (l[k] >= l[j]) and (l[j] != 0):
                    cnt += 1
                    if cnt == s[x] and l[k] not in per:
                        per[x] = l[k]
                        l[k] = 0
                        found = True
                        break
            if found:
                break
    return per


s1 = [4, 4, 2, 0, 1, 0]
print("s1=", s1)
if find_per(s1)[0] == 0:
    print("There is no permutation")
else:
    print("Permutation of s1=", find_per(s1))

s2 = [0, 0, 2, 2, 1, 0]
print("s2=", s2)
if find_per(s2)[0] == 0:
    print("There is no permutation")
else:
    print("Permutation of s2=", find_per(s2))