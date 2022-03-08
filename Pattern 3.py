T = int(input())
for i in range(T):
    P = input()
    a = [0] *len(P)
    k = 0
    for q in range(1, len(P)):
        while k > 0 and P[k] != P[q]:
            k = a[k - 1]
        if P[k] == P[q]:
            k += 1
        a[q] = k
    print(len(a) - a[-1])
