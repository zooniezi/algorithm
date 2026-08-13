def solution(m, n, startX, startY, balls):
    answer = []
    for now_ball in balls:
        targetX, targetY = now_ball
        candidates = []

        if not (startY == targetY and startX >= targetX):
            candidates.append((targetX+startX)**2 + (targetY-startY)**2)

        if not (startY == targetY and startX <= targetX):
            candidates.append((m-targetX+m-startX)**2 + (targetY-startY)**2)

        if not (startX == targetX and startY >= targetY):
            candidates.append((targetX-startX)**2 + (targetY+startY)**2)

        if not (startX == targetX and startY <= targetY):
            candidates.append((targetX-startX)**2 + (n-targetY+n-startY)**2)

        answer.append(min(candidates))
    
    return answer