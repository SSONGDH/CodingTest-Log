# 알고리즘 패턴 템플릿

## BFS

```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```

**격자(맵) 최단거리** (게임 맵 최단거리)

```python
from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]     # 0 = 미방문, 값 = 지나온 칸 수
    dist[0][0] = 1
    q = deque([(0, 0)])                    # 대괄호로 감싸서 시작
    while q:
        r, c = q.popleft()
        if (r, c) == (n - 1, m - 1):
            return dist[r][c]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1   # 넣는 순간 방문 표시
                q.append((nr, nc))              # 튜플 하나
    return -1
```

- **최단거리 / 최소 이동 횟수 → BFS** (DFS는 최단 보장 X)
- 체크리스트
  - `maps[행][열]` 순서
  - 범위 `0 <= r < n` (`-1` 없음)
  - 큐에 **넣을 때** 방문 표시
  - `append((a, b))` 소괄호 두 겹

## DFS

**재귀 함수 만드는 순서**

1. 함수가 들고 다닐 정보 정하기 (몇 번째인지, 지금까지의 값)
2. **종료 조건 먼저** 쓰기 (없으면 `RecursionError`)
3. 선택지마다 다음 단계로 자기 자신 호출
4. 돌아온 결과 합치기

**선택지 탐색형** (타겟 넘버: 숫자마다 +/-)

```python
def dfs(i, total):
    if i == len(numbers):                  # 종료 조건
        return 1 if total == target else 0
    return dfs(i + 1, total + numbers[i]) + dfs(i + 1, total - numbers[i])

dfs(0, 0)
```

**그래프 탐색형** (방문 체크)

```python
def dfs(node, graph, visited):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, graph, visited)
```

**연결된 덩어리 개수 세기** (네트워크, 섬의 개수)

```python
visited = [False] * n
answer = 0
for i in range(n):
    if not visited[i]:      # 처음 보는 곳에서
        dfs(i)              # 연결된 곳 전부 방문 표시
        answer += 1         # 덩어리 하나 추가
```

- 바깥 `for` = 시작점 고르기, 안쪽 `dfs`/`bfs` = 덩어리 하나 다 칠하기
- 인접 행렬(`computers[cur][nxt] == 1`)이면 `for nxt in range(n)`으로 연결 확인

- 안쪽 함수에서 바깥 변수를 **수정**하려면 `nonlocal 변수명`
- 깊이가 깊으면 `import sys; sys.setrecursionlimit(10**6)`

## 완전 탐색 (브루트포스)

**먼저 경우의 수 계산** → 대략 1억 번 이하면 전부 돌아도 됨 (파이썬은 1000만~2000만 번이 안전)

| 형태 | 방법 | 쓴 문제 |
|---|---|---|
| N개 중 K개 고르기 | `combinations(arr, K)` | 블랙잭 |
| 답의 범위가 작게 주어짐 | 범위 전체를 대입 | 수학은 비대면강의입니다, 분해합 |
| N번째 ~인 수 | 1씩 늘리며 조건 확인, 개수 세기 | 영화감독 숌 |
| 큰 판에서 고정 크기 영역 고르기 | 시작점 이중 for문 + 영역 검사 함수 | 체스판 다시 칠하기 |

**N개 중 3개 고르기** (블랙잭)

```python
from itertools import combinations

best = 0
for comb in combinations(nums, 3):     # 순서 없이 한 번씩
    total = sum(comb)
    if total <= limit:
        best = max(best, total)
```

- 3중 for문으로 쓸 때는 `range(i + 1, n)`, `range(j + 1, n)`으로 시작해야 같은 조합 중복 없음

**찾으면 바로 끝내기**: 이중 for문은 `break` 하나로 안 빠져나옴 → 함수로 만들어 `return`

```python
def solve():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                return x, y
```

- 경우의 수가 너무 많으면 범위를 줄일 수 있는지 먼저 생각 (분해합: `N - 9 * 자릿수`부터)
- 공식으로 바로 계산되는 문제를 반복으로 풀고 있지 않은지 확인 (세 막대)

## 이분 탐색

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## 투 포인터

## DP

## 그리디

**지금 가장 좋아 보이는 것부터 고르기**. 큰 단위를 최대한 많이 쓰는 문제에 자주 나옴

**큰 단위부터 줄여 가며 확인** (설탕 배달: 3kg, 5kg 봉지 최소 개수)

```python
answer = -1
for five in range(n // 5, -1, -1):     # 큰 봉지를 많이 쓰는 것부터
    rest = n - 5 * five
    if rest % 3 == 0:                  # 나머지를 작은 봉지로 딱 나누면
        answer = five + rest // 3      # 처음 찾은 게 최소
        break
```

- 큰 단위 개수가 정해지면 작은 단위 개수는 나머지로 계산됨 → 이중 for문 필요 없음
- 동전처럼 큰 단위가 작은 단위의 배수가 아니면 무조건 큰 것부터가 틀릴 수 있음 → 위처럼 "나머지가 나눠지는지" 확인하거나 DP
