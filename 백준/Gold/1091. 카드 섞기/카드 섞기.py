N = int(input())

whichPlayer = list(map(int,input().split()))
shuffle = list(map(int,input().split()))
card = [i for i in range(N)]
ans = 0

def shuffled(card, shuf):
    temp = [i for i in range(N)]
    for i in range(N):
        temp[shuf[i]] = card[i]   
    return temp

while True:
    check = True
    for i in range(N):
        if i%3 != whichPlayer[card[i]]:
            check = False
            break
    if check:
        print(ans)
        break
    else:
        card = shuffled(card,shuffle)
        ans += 1
        if card == [i for i in range(N)]:
            print(-1)
            break
    
