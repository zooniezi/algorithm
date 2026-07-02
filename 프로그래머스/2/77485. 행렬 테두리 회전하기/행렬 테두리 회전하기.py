def solution(rows, columns, queries):
                
    answer = []
    
    #행렬 만들어 놓기
    arr = [[0 for _ in range(columns)] for __ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i*columns+(j+1)
    #queries에 있는 애들 불러오기
    
    for each in queries:
        #index로 변환
        x1,y1,x2,y2 = each[0]-1, each[1]-1, each[2]-1, each[3]-1
        #변환 예정인 애들 저장하면서 최솟값 추적
        candidates = []
        min_num = 10001
        temp = arr[x1][y1]
        temp2 = arr[x1][y1]
        for i in range(y1+1,y2+1):
            min_num = min(min_num, arr[x1][i])
            temp2 = arr[x1][i] 
            arr[x1][i] = temp
            temp = temp2
            candidates.append(arr[x1][i])
        for i in range(x1+1,x2+1):
            min_num = min(min_num, arr[i][y2])
            temp2 = arr[i][y2]
            arr[i][y2] = temp
            temp = temp2
            candidates.append(arr[i][y2])
        for i in range(y2-1,y1-1,-1):
            min_num = min(min_num, arr[x2][i])
            temp2 = arr[x2][i]
            arr[x2][i] = temp
            temp = temp2
            candidates.append(arr[x2][i])
        for i in range(x2-1,x1-1,-1):
            min_num = min(min_num, arr[i][y1])
            temp2 = arr[i][y1]
            arr[i][y1] = temp
            temp = temp2
            candidates.append(arr[i][y1])
        
        answer.append(min_num)
            
            

    return answer