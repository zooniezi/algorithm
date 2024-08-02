n = int(input())
white, blue = 0,0

paper = [[list(map(int, input().split())) for _ in range(n)]]

def cutpaper(paper,size):
    paper1 = []
    paper2 = []
    paper3 = []
    paper4 = []
    newsize = size//2
    for i in range(newsize):
        paper1.append(paper[i][:newsize])
        paper2.append(paper[i][newsize:])
        paper3.append(paper[newsize+i][:newsize])
        paper4.append(paper[newsize+i][newsize:])
    papers = [paper1, paper2, paper3, paper4]
    return papers

while paper:
    nowpaper = paper.pop()
    nowsize = len(nowpaper)
    color = nowpaper[0][0]
    is_single_color = True
    for i in range(nowsize):
        for j in range(nowsize):
            if nowpaper[i][j] != color:
                is_single_color = False
                newpaper = cutpaper(nowpaper, nowsize)
                for each in newpaper:
                    paper.append(each)
                break
        if not is_single_color:
            break
    
    if is_single_color:
        if color == 1:
            blue+=1
        else:
            white+=1

print(white)
print(blue)