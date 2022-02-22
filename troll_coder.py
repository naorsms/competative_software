x= int(input())
array = []
for i in range(x):
     array.append(0)
array.insert(0, 'Q')
print(" ".join(map(str, array)))
sum_correct = int(input())
change = sum_correct
i = 1
while(sum_correct < x):
   if(array[i] == 0):
       array[i] = 1
   else:
       array[i] = 0
   print(" ".join(map(str, array)))
   sum_correct = int(input())
   if(sum_correct < change):
       if (array[i] == 0):
           array[i] = 1
       else:
           array[i] = 0
       sum_correct = change
   i += 1
   change = sum_correct
array[0] = "A"
print(" ".join(map(str, array)))

