data = input()
N = int(data.split(" ")[0])
M = int(data.split(" ")[1])
S = int(data.split(" ")[2])
sumall = 0
low = 2
high = N
while(low <= high):
    mid = (high + low)//2
    sum = (mid - (low - 1))*M + S
    low = mid + 1
    sumall += sum
print(sumall)

