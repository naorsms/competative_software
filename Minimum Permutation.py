data = input()
N = int(data.split(" ")[0])
M = int(data.split(" ")[1])
a = input().strip().split(' ')
s = input().strip().split(' ')
A = [int(p) for p in a]
S = [int(p) for p in s]
S.sort()
i = 0
j = 0
while i < N+j and j < M :
   if A[i] > S[j]:
      A.insert(i, S[j])
      j+=1
   else:
      i+=1
while j<M:
   A.append(S[j])
   j += 1
print(" ".join(map(str, A)))

