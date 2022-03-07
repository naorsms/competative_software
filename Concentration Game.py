N = int(input())
cards = []
for i in range(N+1):
    cards.append(0)
for i in range(1,2*N,2):
    print(i," ",i + 1)
    x = input()
    if x == 'MATCH':
        continue
    for j in range(2):
        card = (int(x.split(" ")[j]))
        if cards[card] == 0:
           cards[card] = i + j
        else:
            print(cards[card]," ",i + j)
            input()
print (-1)
