# 게임 맵 최단거리

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: 성공 (에러 원인 AI에게 질문 후 수정)

## 접근 방법

- 최단거리 = **BFS** (가까운 칸부터 퍼져 나가므로 처음 도착한 순간이 최단거리)
- 큐에 `(x, y, 지금까지 지나온 칸 수)`를 넣고, 상하좌우로 갈 수 있는 칸을 큐에 추가
- 한 번 넣은 칸은 `visited`로 표시해서 다시 넣지 않음
- 이웃 칸이 도착 지점이면 `distance + 1` 반환, 큐가 다 비면 도착 불가 → `-1`

## 막혔던 부분

처음 코드에서 `ValueError: not enough values to unpack (expected 3, got 1)` 에러가 났고, 고치면서 실수 4개를 찾음

### 1. `append`에 대괄호를 씀 (에러 원인)

```python
queue.append([(nx, ny, distance + 1)])   # X: 리스트 1개가 통째로 들어감
queue.append((nx, ny, distance + 1))     # O: 튜플 1개
```

- 대괄호를 쓰면 큐에 `[(nx, ny, d)]`라는 리스트 하나가 들어감
- 다음에 `x, y, distance = queue.popleft()` 하면 꺼낸 값이 리스트 1개라서 3개로 나눌 수 없음 → `expected 3, got 1`

### 2. `maps[x][y]`로 접근함

```python
maps[nx][ny]   # X
maps[ny][nx]   # O: maps[행][열] = maps[y][x]
```

- 2차원 리스트는 **`maps[행][열]`**. 행 = 세로 위치 = `y`, 열 = 가로 위치 = `x`
- 헷갈리면 처음부터 `x`, `y` 대신 `r`(row), `c`(col)로 이름 짓기

### 3. 범위 조건에 `-1`을 붙임

```python
nx < len(maps[0]) - 1   # X: 맨 오른쪽 열을 못 감
nx < len(maps[0])       # O
```

- 인덱스는 `0` ~ `길이-1`이므로 조건은 `0 <= nx < 길이`
- `visited` 만들 때도 `-1`을 붙여서 크기가 모자랐음

### 4. 큐에 넣을 때 `visited` 표시를 안 함

```python
queue.append((nx, ny, distance + 1))
visited[ny][nx] = True        # 넣는 순간 바로 표시
```

- 표시를 안 하면 같은 칸이 큐에 여러 번 들어가서 시간 초과

### 도착 지점 계산

- `end = (len(maps[0]), len(maps))`는 **크기**라서 실제 마지막 인덱스는 `(ex-1, ey-1)`

## 다른 풀이에서 배운 점

### 정리된 BFS 풀이

```python
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])          # n: 행 개수(세로), m: 열 개수(가로)
    dist = [[0] * m for _ in range(n)]      # 0이면 아직 안 감, 값 = 지나온 칸 수
    dist[0][0] = 1

    q = deque([(0, 0)])                     # (행, 열)
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == m - 1:       # 꺼낸 칸이 도착 지점이면 끝
            return dist[r][c]

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return -1
```

- `visited`와 거리를 `dist` 하나로 합침 (0이면 미방문)
- **꺼낸 직후** 도착 확인하면 도착 칸이 벽인지 따로 신경 쓸 필요 없음
- `0 <= nr < n`처럼 범위 조건을 이어서 쓸 수 있음
- `maps[nr][nc] == 1`을 범위 검사 **뒤에** 써야 함 (범위 밖 인덱스 접근 방지)

### 왜 DFS가 아니라 BFS인가

- BFS는 거리 1인 칸 → 거리 2인 칸 → … 순서로 퍼짐 → 처음 도착한 거리가 최단
- DFS는 한 길을 끝까지 가서 돌아오기 때문에 처음 도착한 길이 최단이라는 보장이 없음
- **"최단거리", "최소 이동 횟수"가 나오면 BFS**
