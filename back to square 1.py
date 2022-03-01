n = int(input())
props = []
while(n > 0):
    if(n == 1):
        print(1)
        n = int(input())
        continue
    prop = input()
    for i in range(n-1):
        props.insert(i,float(prop.split(" ")[i]))
    sum = 1
    res = 1
    for i in range(n-1,0,-1):
       sum = sum/props[i-1]
       res += sum
    print(round(res))
    n = int(input())




