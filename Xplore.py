import json
n = int(input())
dic = {}
names = []
for _ in range(n):
    data = json.loads(input())
    for author in data['authors']['authors']:
        name = author['full_name']
        if name not in dic:
            dic[name] = [data['citing_paper_count']]
            names.append(name)
        else:
            dic[name].append(data['citing_paper_count'])
answer = {}
for name in range(len(dic)):
    x = sorted(dic[names[name]],reverse=True)
    leng  = len(x)
    print(x)
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

