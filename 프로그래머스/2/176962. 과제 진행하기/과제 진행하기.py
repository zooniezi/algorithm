def solution(plans):
    # 시간을 분으로 변환
    def to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    
    # 시간순 정렬
    plans = sorted(plans, key=lambda x: to_min(x[1]))
    
    result = []
    stack = []  # 멈춘 과제 스택
    
    for i in range(len(plans)):
        name, start, playtime = plans[i][0], to_min(plans[i][1]), int(plans[i][2])
        
        # 다음 과제 시작 시각
        next_start = to_min(plans[i+1][1]) if i + 1 < len(plans) else float('inf')
        
        # 현재 과제 종료 시각
        end = start + playtime
        
        if end <= next_start:
            # 현재 과제를 다음 과제 시작 전에 끝낼 수 있음
            result.append(name)
            
            # 남은 시간으로 스택에 있는 과제 처리
            remaining_time = next_start - end
            while stack and remaining_time > 0:
                prev_name, prev_time = stack[-1]
                if prev_time <= remaining_time:
                    remaining_time -= prev_time
                    result.append(prev_name)
                    stack.pop()
                else:
                    stack[-1] = (prev_name, prev_time - remaining_time)
                    remaining_time = 0
        else:
            # 다음 과제 시작 전에 못 끝냄 → 스택에 남은 시간 push
            stack.append((name, end - next_start))
    
    # 스택에 남은 과제 처리 (역순으로 꺼내기)
    while stack:
        result.append(stack.pop()[0])
    
    return result