string_num = int(input())
dic = dict()

for n in range(string_num):
    coupon = input().replace('-', '')
    for i in range(len(coupon)):
        string = coupon[:i] + "*" + coupon[i + 1:]
        if string in dic:
            dic[string] += 1
        else:
            dic[string] = 1
        print(dic)
Sum = 0
for index in dic:
    appearances = dic[index]
    if appearances > 1:
        for i in range(1, appearances):
            Sum += i
print(Sum)