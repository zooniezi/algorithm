def solution(players, m, k):
    answer = 0
    
    # 각 시간대에 사용 가능한 서버 수
    active_server = [0 for i in range(len(players))]
    
    for i in range(len(players)):
        # 현재 필요한 서버 수
        need_server = players[i] // m
        
        # 이미 운영 중인 서버로 충분한 경우
        if active_server[i] >= need_server:
            continue
        
        # 추가로 증설해야 하는 서버 수
        add_server = need_server - active_server[i]
        answer += add_server
        
        # k시간 동안 서버 유지
        for j in range(i, min(i + k, len(players))):
            active_server[j] += add_server
    
    return answer