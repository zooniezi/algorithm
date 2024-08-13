num_dice = int(input())
dices = []
for i in range(num_dice):
    dices.append(list(map(int, input().split())))

arr = []
for value in range(1,7):
    now_idx = 0
    next_idx = 0
    temp = 0
    for idx in range(6):
        if dices[0][idx] == value:
            now_idx = idx
            if idx == 0 or idx == 5:
                next_idx = 5-idx
            elif idx == 1 or idx == 3:
                next_idx = 4-idx
            else:
                next_idx = 6-idx
            break
    if dices[0][now_idx] == 6:
        if dices[0][next_idx] == 5:
            temp+=4
        else:
            temp+=5
    elif dices[0][now_idx] == 5:
        if dices[0][next_idx] == 6:
            temp += 4
        else:
            temp += 6
    else:
        if dices[0][next_idx] == 6:
            temp += 5
        else:
            temp += 6

    
    for now in range(1,num_dice):
        for idx in range(6):
            if dices[now][idx] == dices[now-1][next_idx]:
                now_idx=idx
                break
        if now_idx == 0 or now_idx == 5:
            next_idx = 5-now_idx
        elif now_idx == 1 or now_idx == 3:
            next_idx = 4-now_idx
        else:
            next_idx = 6-now_idx

        if dices[now][now_idx] == 6:
            if dices[now][next_idx] == 5:
                temp+=4
            else:
                temp+=5
        elif dices[now][now_idx] == 5:
            if dices[now][next_idx] == 6:
                temp += 4
            else:
                temp += 6
        else:
            if dices[now][next_idx] == 6:
                temp += 5
            else:
                temp += 6
    arr.append(temp)

print(max(arr))