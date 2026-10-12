# 네트워크

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
- 난이도: Lv.3
- 푼 날짜:
- 소요 시간:
- 결과: AI 풀이 참고 → 다시 풀기 필요 (이해는 했지만 직접 짜기 어려움)

## 접근 방법

- **네트워크 개수 = 서로 연결된 덩어리 개수**
- 0번 컴퓨터부터 차례로 보면서, 아직 방문 안 한 컴퓨터를 만나면
  1. 새 네트워크 발견 → `answer += 1`
  2. 그 컴퓨터에서 연결된 컴퓨터를 **전부** 따라가며 방문 표시 (스택 DFS)
- 이미 방문한 컴퓨터는 앞에서 센 네트워크에 속하므로 건너뜀

## 막혔던 부분

- 처음에 감이 안 와서 AI 풀이를 참고함
- 다시 풀어 보니 흐름은 이해되는데 코드로 옮기기가 어려움

## 다른 풀이에서 배운 점

### 문제를 그림으로 바꾸기

`computers = [[1,1,0], [1,1,0], [0,0,1]]`

```
computers[i][j] == 1 → i번과 j번이 연결됨

    0  1  2
0 [ 1, 1, 0 ]     0 ─ 1      2
1 [ 1, 1, 0 ]
2 [ 0, 0, 1 ]     덩어리 2개 → 답 2
```

- `computers[current][j]`: `current`번 컴퓨터의 줄을 보면서 `j`번과 연결됐는지 확인
- 대각선(`computers[i][i]`)은 자기 자신이라 항상 1이지만, 이미 `visited`라서 다시 안 넣음
  - 코드 주석의 "자기 자신이 아니고"는 `visited` 체크가 대신 처리하는 것

### 빈 화면에서 짜는 순서

외우려 하지 말고 **이 순서대로 한 줄씩** 써 보기

**① 바깥 틀: "방문 안 한 컴퓨터를 만나면 개수 +1"**

```python
def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            # 여기서 i와 연결된 애들을 전부 방문 표시
            answer += 1
    return answer
```

- 여기까지가 문제의 핵심 아이디어. 안쪽 탐색은 다음 단계에서 채움

**② 안쪽: "i와 연결된 애들 전부 방문 표시" = 탐색 하나**

```python
stack = [i]                 # 시작점 넣고
visited[i] = True           # 넣자마자 방문 표시
while stack:                # 빌 때까지
    cur = stack.pop()       # 하나 꺼내서
    for nxt in range(n):    # 모든 컴퓨터 중
        if computers[cur][nxt] == 1 and not visited[nxt]:  # 연결됐고 처음 보면
            visited[nxt] = True
            stack.append(nxt)
```

- 게임 맵 최단거리 BFS와 **모양이 똑같음**
  - 다른 점 1: 이동이 상하좌우가 아니라 `computers[cur][nxt] == 1`인 `nxt`
  - 다른 점 2: 거리는 필요 없고 방문 표시만

**③ ①의 주석 자리에 ②를 끼워 넣으면 완성**

### 재귀 DFS 풀이

탐색 부분을 함수로 빼면 바깥 틀이 더 잘 보임

```python
def solution(n, computers):
    visited = [False] * n

    def dfs(cur):
        visited[cur] = True
        for nxt in range(n):
            if computers[cur][nxt] == 1 and not visited[nxt]:
                dfs(nxt)

    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)          # i와 연결된 덩어리 전체를 방문 표시
            answer += 1
    return answer
```

### 큐 BFS 풀이

스택 대신 큐를 써도 결과는 같음 (방문 순서만 다름)

```python
from collections import deque

stack = [i]          →   q = deque([i])
cur = stack.pop()    →   cur = q.popleft()
stack.append(nxt)    →   q.append(nxt)
```

- 이 문제는 "전부 방문"만 하면 되니 DFS든 BFS든 상관없음
- **최단거리**가 필요할 때만 BFS여야 함

### 같은 유형 알아보는 법

- "연결된 그룹이 몇 개", "섬의 개수", "영역 개수" → **방문 안 한 곳에서 탐색 시작할 때마다 +1**
