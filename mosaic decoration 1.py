num_and_prices = input()
num = int(num_and_prices.split(' ')[0])
black = int(num_and_prices.split(' ')[1])
pink = int(num_and_prices.split(' ')[2])
amount = []
black_pile = 0
pink_pile = 0
sum = 0
for bathrooms in range(num):
    num_of_piles = input()
    black_pile += float(num_of_piles.split(' ')[0])
    pink_pile += float(num_of_piles.split(' ')[1])
if black_pile%10 == 0:
    sum += black * black_pile/10
else:
    sum += black * (int(black_pile/10)+1)
if pink_pile % 10 == 0:
    sum += int(pink * pink_pile / 10)
else:
    sum += pink * (int(pink_pile / 10) + 1)
print(int(sum))