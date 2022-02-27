import json
n = int(input())
dic = {}
names = []
for index in range(n):
    data = json.loads(input())
    for author in data['authors']['authors']:
        if author['full_name'] not in names:
            dic[author['full_name']] = [data['citing_paper_count']]
            names.append(author['full_name'])
        else:
            dic[author['full_name']].append(data['citing_paper_count'])
answer = {}
for name in range(len(dic)):
    x = sorted(dic[names[name]],reverse=True)
    leng  = len(x)
    answer[names[name]] = ' '
    for j in range(leng):
        if x[j] < j +1:
            answer[names[name]] = j
            break
    if answer[names[name]] == ' ':
        answer[names[name]] = j + 1
answersort = sorted(answer.items(), key=lambda x:(-x[1],x[0]))
le = len(answersort)
for i in range(le):
    print(answersort[i][0],answersort[i][1])
