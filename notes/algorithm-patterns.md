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

- 안쪽 함수에서 바깥 변수를 **수정**하려면 `nonlocal 변수명`
- 깊이가 깊으면 `import sys; sys.setrecursionlimit(10**6)`

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
