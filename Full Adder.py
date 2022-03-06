data = input()
print1 = input()
print2 = input()
print3 = input()
print4 = input()
base = int(data.split(" ")[0])
num = data.split(" ")[1]
nums = {}
for i in range(base):
    nums[num[i]] = i
nums[" "] = 0
sumall = ""
flag = 0
for i in range(len(print1)-1,0,-1):
    sum = 0
    sum += nums[print1[i]]+nums[print2[i]] + flag
    if sum >= base:
        flag = 1
        sum = sum%base
    else:
        flag = 0
    sumall += num[sum]
print(data)
print(print1)
print(print2)
print(print3)
print(" " + ''.join(reversed(sumall)))
