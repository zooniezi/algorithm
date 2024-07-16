testcase = int(input())
for i in range(testcase):
    startend = list(map(int, input().split()))
    planetNum = int(input())
    count = 0
    #행성계별로 출발점, 도착점을 내포하는지 확인하기
    for i in range(planetNum):
        x,y,r = map(int, input().split())
        pointX = (startend[0]-x)*(startend[0]-x)+(startend[1]-y)*(startend[1]-y)
        pointY = (startend[2]-x)*(startend[2]-x)+(startend[3]-y)*(startend[3]-y)
        if pointX<r*r and pointY<r*r:
            continue
        elif pointX<r*r:
            count+=1
        elif pointY<r*r:
            count+=1
    print(count)
