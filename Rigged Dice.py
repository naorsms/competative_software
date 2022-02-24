games_num = int(input())
#print("d",games_num)
for games in range(games_num):
    alice_total = 0
    bob_total = 0
    rigged_dice = 1
    die1 = []
    die2 = []
    rounds_num = int(input())
    for rounds in range(rounds_num):
        scores = input()
        #print("t",scores)
        alice_score = int(scores.split(" ")[0])
        bob_score = int(scores.split(" ")[1])
        alice_total += alice_score
        bob_total += bob_score
        if rigged_dice == 1:
            die1.append(alice_score)
            die2.append(bob_score)
        elif rigged_dice == -1:
            die1.append(bob_score)
            die2.append(alice_score)
        if alice_total != bob_total:
            rigged_dice *= -1
    Sum1 = sum(die1)
    Sum2 = sum(die2)
    if Sum1 > Sum2:
        print(1)
    else:
        print(2)
