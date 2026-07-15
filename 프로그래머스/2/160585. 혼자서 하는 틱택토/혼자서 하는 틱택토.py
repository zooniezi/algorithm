def solution(board):
    countO = 0
    countX = 0
    checkO = 0
    checkX = 0
    is_checkmate = [
                    [[0,0],[0,1],[0,2]],
                    [[1,0],[1,1],[1,2]],
                    [[2,0],[2,1],[2,2]],
                    [[0,0],[1,0],[2,0]],
                    [[0,1],[1,1],[2,1]],
                    [[0,2],[1,2],[2,2]],
                    [[0,0],[1,1],[2,2]],
                    [[0,2],[1,1],[2,0]]
                    ]
    # O 와 X 개수 확인해서 차례가 지켜졌는지 여부 확인하기
    for each_line in board:
        for each_box in each_line:
            if each_box == "O":
                countO += 1
            if each_box == "X":
                countX += 1
    
    if countO-countX != 0 and countO-countX != 1:
        return 0
    
    #게임이 누군가의 승리로 끝났는지를 확인하기
    for check_checkmate in is_checkmate:
        temp = 1
        for now_coordinate in check_checkmate:
            if board[now_coordinate[0]][now_coordinate[1]] != "O":
                temp = 0
                break
        if temp:
            checkO += 1
        
    for check_checkmate in is_checkmate:
        temp = 1
        for now_coordinate in check_checkmate:
            if board[now_coordinate[0]][now_coordinate[1]] != "X":
                temp = 0
                break
        if temp:
            checkX += 1
    
    #O가 승리하는 경우 -> O가 X보다 1개 많이 두고, checkO은 1, checkX는 0
    if countO == countX+1 and checkO >= 1 and checkX == 0:
        return 1
    #X가 승리하는 경우 -> O와 X가 같은 개수를 두고, checkO은 0, checkX는 1
    elif countO == countX and checkO == 0 and checkX >= 1:
        return 1
    #게임이 진행중인 경우에, checkO, checkX가 둘다 0인지 확인하기
    elif checkO == 0 and checkX == 0:
        return 1
    else:
        return 0
    
    