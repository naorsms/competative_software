T = int(input())
"kfir"
for i in range(T):
    P = input()
    m = len(P)
    a = [0] * m
    k = 0

    for q in range(2, m + 1):
        print("k: ",k,"pk: ",P[k],"pq: ",P[q-1],"ak: ",a[k-1])
        while k > 0 and P[k] != P[q - 1]:
            k = a[k - 1]
        if P[k] == P[q - 1]:
            k += 1
        a[q - 1] = k

    print(m - a[m-1])