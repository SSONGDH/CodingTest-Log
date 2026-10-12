def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문 여부 체크 리스트
    
    for i in range(n):
        # 이미 다른 네트워크 탐색 때 방문했다면 건너뜁니다.
        if visited[i]:
            continue
            
        # 1. 새로운 컴퓨터를 발견하면 네트워크 개수를 1 늘립니다.
        answer += 1
        
        # 2. 이 컴퓨터와 연결된 모든 컴퓨터를 찾기 위한 스택을 만듭니다.
        stack = [i]
        visited[i] = True  # 시작 컴퓨터 방문 처리
        
        # 3. 스택이 빌 때까지 연결된 컴퓨터들을 끝까지 추적합니다.
        while stack:
            current = stack.pop()  # 현재 조사할 컴퓨터 번호를 꺼냅니다.
            
            for j in range(n):
                # 자기 자신이 아니고, 연결되어 있으며, 아직 방문하지 않은 컴퓨터라면
                if computers[current][j] == 1 and not visited[j]:
                    visited[j] = True  # 방문 도장을 찍고
                    stack.append(j)    # 다음에 조사하기 위해 스택에 넣습니다.
                    
    return answer
