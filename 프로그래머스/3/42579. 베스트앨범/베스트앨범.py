def solution(genres, plays):
    dict = {}
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]][0] += plays[i]
            dict[genres[i]][1].append([plays[i],i])
        else:
            dict[genres[i]] = [plays[i],[[plays[i],i]]]
    d2 = sorted(dict.items(), key = lambda x: x[1], reverse= True)
    answer = []
    for each in d2:
        now = sorted(each[1][1], key = lambda x: x[0], reverse = True)
        for i in range(len(now)):
            if i == 2:
                break
            else:
                answer.append(now[i][1])
                
    return answer