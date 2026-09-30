def solution(edges):
    answer = [0,0,0,0]
    #[a,b] 에서 a는 나가는 edge 수, b는 들어오는 edge 수
    graphs = {}
    for edge in edges:
        if edge[0] in graphs.keys():
            graphs[edge[0]][0] += 1
        else:
            graphs[edge[0]] = [1,0]
        if edge[1] in graphs.keys():
            graphs[edge[1]][1] += 1
        else:
            graphs[edge[1]] = [0,1]
            
    for each in graphs.keys():
        if graphs[each][0] >= 2 and graphs[each][1] == 0:
            answer[0] = each
        if graphs[each][0] == 0:
            answer[2] += 1
        if graphs[each][0] == 2 and graphs[each][1] >= 2:
            answer[3] += 1
    answer[1] = graphs[answer[0]][0] - (answer[2]+answer[3])
    return answer