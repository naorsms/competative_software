def values(x,y):
    if x == 'R':
        if y == 'R':
            return 50
        elif y == 'A':
            return 20
        elif y == 'Q' or y == 'K' or y == 'J':
            return 15
        elif y == 'T':
            return 10
        else:
            return int(y)

    elif y == 'R':
        if x == 'A':
            return 20
        elif x == 'Q' or x == 'K' or x == 'J':
            return 15
        elif x == 'T':
            return 10
        else:
            return int(x)

    elif x == 'A':
        return 20
    elif x == 'Q' or x == 'K' or x == 'J':
        return 15
    elif x == 'T':
        return 10
    else:
        return int(x)
arr = [[0] * (1001) for i in range(1001)]

def equal(x):
    if x == 'A':
        return 20
    elif x == 'R':
        return 50
    elif x == 'Q' or x == 'K' or x == 'J':
        return 15
    elif x == 'T':
        return 10
    else:
        return int(x)

n = int(input())
while n != 0:
    #rows, cols = n+1, n+1
    #arr = [[0]*cols]*rows

    lcs1 = []
    lcs2 = []
    data = input()
    lcs1.append(0)
    check_lcs1 = True
    for i in range(n):
        lcs1.append((data.split(" ")[i]))
        if i > 1:
            if lcs1[i] != lcs1[i-1]:
                check_lcs1 = False
    data = input()
    lcs2.append(0)
    check_lcs2 = True
    for i in range(n):
        lcs2.append((data.split(" ")[i]))
        if i > 1:
            if lcs2[i] != lcs2[i-1]:
                check_lcs2 = False
    if lcs2 == True and lcs1 == True:
        if lcs1 == lcs2:
            print(equal(lcs1[1])*2*n)
            continue
        elif lcs1[1] == 'R':
            print(equal(lcs2[1])*n*2)
            continue
        elif lcs2[1] == 'R':
            print(equal(lcs1[1])*n*2)
            continue
        else:
            print(0)
            continue
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = max(arr[i][j-1],arr[i-1][j])
            if lcs1[i] == lcs2[j] or lcs1[i] == 'R' or lcs2[j] == 'R':
                arr[i][j] = max(arr[i-1][j-1]+values(lcs1[i],lcs2[j]),arr[i][j])

    print(arr[n][n]*2)
    n = int(input())

