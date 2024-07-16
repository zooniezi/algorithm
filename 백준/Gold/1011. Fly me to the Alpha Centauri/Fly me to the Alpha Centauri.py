testcase = int(input())
for i in range(testcase):
    x, y = map(int, input().split())
    length = y-x
    count = 0
    movement = 1
    moveLength = 0
    while moveLength < length:
        count+=1
        moveLength+=movement
        if count%2 == 0:
            movement += 1
    print(count)