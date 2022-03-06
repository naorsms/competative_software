
data = input()
W = int(data.split(" ")[0])
H = int(data.split(" ")[1])
A = int(data.split(" ")[2])
B = int(data.split(" ")[3])
M = int(data.split(" ")[4])
C = int(data.split(" ")[5])
width_of_wall = W//A
height_of_wall = H//B
cuts = 0
if W%A != 0:
    cuts += H
    width_of_wall += 1
if H%B != 0:
    cuts += W
    height_of_wall +=1
area = width_of_wall*height_of_wall
if area%10 == 0:
    sum = area//10
else:
    sum = area//10+1
print(sum*M + cuts*C)

