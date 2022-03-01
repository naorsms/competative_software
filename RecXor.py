# def f(a):
#     if a%4 == 0:
#         return a
#     elif a%4 == 1:
#         return 1
#     elif a%4 == 2:
#         return a + 1
#     return 0


def xor(a, b):
    if a % 4 == 0:
        a = a
    elif a % 4 == 1:
        a = 1
    elif a % 4 == 2:
        a += 1
    else:
        a = 0
    if b % 4 == 0:
        b = b
    elif b % 4 == 1:
        b = 1
    elif b % 4 == 2:
        b += 1
    else:
        b = 0
    return a^b


N = int(input())
for N in range(N):
    var = input()
    l = int(var.split(" ")[0])
    h = int(var.split(" ")[1])
    n = int(var.split(" ")[2])
    d1 = int(var.split(" ")[3])
    d2 = int(var.split(" ")[4])
    width_start = (d1-n) % l + 1
    width_end = (d2-n) % l + 1
    height_start = (d1-n) // l + 1
    height_end = (d2-n) // l + 1
    cells_num = l * h

    if width_start > width_end:
        width_start, width_end = width_end, width_start

    if height_start > height_end:
        height_start, height_end = height_end, height_start

    inner_square = 0
    for i in range(height_start,height_end +1):
        x = n + width_start-1 + (i-1)*l
        y = n + width_end -1 + (i-1)*l
        inner_square ^= xor(n + width_start-2 + (i-1)*l,n + width_end -1 + (i-1)*l)

    whole_square = xor(l*h + n -1,n-1)
    print(whole_square^inner_square)
