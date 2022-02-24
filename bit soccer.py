data = input()
text = input().strip().split(' ')
players = [int(p) for p in text]
Q = int(input())
for i in range(Q):
    goal_team_performance = int(input())
    goal_team = 0
    for player in players:
        if player|goal_team_performance == goal_team_performance:
            goal_team = goal_team|player
    if goal_team == goal_team_performance:
       print("YES")
    else:
       print("NO")