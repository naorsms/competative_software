import math
radius = float(input())
i = 0
dict = {}
while i < 26:
    parse = input()
    dict[parse.split(" ")[0]] = float(parse.split(" ")[1])
    i += 1
sentence = input()
# for index in sentence:
#     if not index.isalpha():
#         sentence = sentence.replace(index,'')
sentence = sentence.upper()
sum = radius
for letter in range(1, len(sentence)):
    if not sentence[letter].isalpha():
        sentence = sentence.replace(sentence[letter], '')
    if letter >= len(sentence):
        break
    angle = abs(dict[sentence[letter]] - dict[sentence[letter-1]])
    if angle > 180:
        angle = 360 - angle
    if angle != 0:
        sum += math.sqrt(2*math.pow(radius,2) - 2*radius*radius*math.cos(math.radians(angle)))

print(math.ceil(sum))