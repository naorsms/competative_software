import math
radius = float(input())

dict = {}
letters = []
find_letter = []
for i in range(26):
    parse= input()
    dict[parse.split(" ")[0]] = float(parse.split(" ")[1])
    letters.append(parse.split(" ")[0])
sentence = input().upper()
for letter in sentence:
    if letter in letters:
         find_letter.append(letter)
arr = []
arr.append(find_letter[0])
for i in range(1, len(find_letter)):
    if find_letter[i] != arr[-1]:
        arr.append(find_letter[i])
sum = radius
for letter in range(1, len(arr)):
    angle = abs(dict[arr[letter]] - dict[arr[letter-1]])
    if angle > 180:
        angle = 360 - angle
    if angle != 0:
        sum += math.sqrt(2*math.pow(radius,2) - 2*radius*radius*math.cos(math.radians(angle)))

print(math.ceil(sum))

