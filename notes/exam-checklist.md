# 시험 직전 체크리스트 (Python)

시험 시작 전에 이 파일만 훑고 들어가기. 자세한 문법은 `python-syntax.md`, 템플릿은 `algorithm-patterns.md`

## 목차

- [1. 필수 라이브러리 & 문법](#1-필수-라이브러리--문법-암기-필수)
- [2. 문항별 접근 전략](#2-문항별-접근-전략)
- [3. 시간 초과 방지 팁](#3-시간-초과-방지-팁)
- [4. 문제 유형 판단표](#4-문제-유형-판단표)

---

## 1. 필수 라이브러리 & 문법 (암기 필수)

### 맨 위에 적고 시작

```python
import sys
sys.setrecursionlimit(10**6)
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
import heapq
```

### collections.deque: 큐 / BFS 필수

```python
q = deque([start])      # 만들 때 대괄호
q.append((x, y))        # 넣을 때 소괄호 두 겹
q.popleft()
```

| | `list.pop(0)` | `deque.popleft()` |
|---|---|---|
| 시간 | O(N) | **O(1)** |

- 탐색 문제에서 리스트를 큐로 쓰면 효율성 테스트에서 탈락

### itertools: 완전탐색 / 조합

```python
list(permutations([1, 2, 3], 2))   # 순열 (순서 O): (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)
list(combinations([1, 2, 3], 2))   # 조합 (순서 X): (1,2) (1,3) (2,3)
list(product([0, 1], repeat=2))    # 중복 순열:     (0,0) (0,1) (1,0) (1,1)
```

- 직접 재귀로 구현하는 것보다 빠르고 실수가 적음
- `r`을 빼먹으면 `permutations(arr)`은 전체 길이 순열

### heapq: 우선순위 큐 / 최단거리 / 그리디

```python
h = []
heapq.heappush(h, 5)       # O(log N)
heapq.heappush(h, 1)
heapq.heappop(h)           # 1  항상 가장 작은 값이 나옴, O(log N)
h[0]                       # 가장 작은 값 확인 (빼지 않음)

heapq.heapify(arr)         # 기존 리스트를 힙으로, O(N)

# 최대 힙: 음수로 넣고 꺼낼 때 다시 음수
heapq.heappush(h, -x)
-heapq.heappop(h)

# 여러 기준: 튜플은 첫 번째 값 기준으로 정렬
heapq.heappush(h, (소요시간, 요청시각))
```

- 최솟값/최댓값을 **계속** 꺼내야 하는 문제(스케줄링, 디스크 컨트롤러, 더 맵게)에서 필수
- 매번 `sort()`나 `min()`을 하면 O(N)씩 들어서 시간 초과

### sys.setrecursionlimit(10**6)

- 파이썬 기본 재귀 깊이 제한은 **1,000회**
- 재귀 DFS에서 이걸 안 적으면 입력이 클 때 `RecursionError` → 런타임 에러
- 그래도 불안하면 재귀 대신 **스택(`list`) DFS**로 (네트워크 풀이 방식)

---

## 2. 문항별 접근 전략

### 1번 문항: 구현 / 문자열 처리

```python
s[::-1]                 # 뒤집기
s.split()               # 공백 기준 쪼개기
s.split(",")            # 구분자 지정
s.replace("a", "b")     # 바꾸기
s.startswith("119")     # 시작 확인
```

- 빈도수 계산, 매칭은 **딕셔너리 해시 맵** (조회 O(1))

```python
count = {}
for x in arr:
    count[x] = count.get(x, 0) + 1
```

- 관련 문제: 완주하지 못한 선수, 의상, 전화번호 목록

### 2번 문항: BFS / DFS 탐색

- **최단거리 → 무조건 BFS (`deque`)**
- **방문 체크 배열(`visited`)** 꼭 만들기 → 안 만들면 같은 곳을 반복 방문해서 시간 초과
- 큐/스택에 **넣는 순간** 방문 표시
- 관련 문제: 게임 맵 최단거리(BFS), 네트워크(DFS), 타겟 넘버(DFS)

### 3번 문항: DP / 그리디 / 이분탐색

| 보이는 것 | 유형 |
|---|---|
| 정렬하고 앞에서부터 처리하면 풀리는 규칙 | **그리디** |
| `dp[i] = dp[i-1] + ...` 같은 점화식 | **DP** |
| 정렬된 데이터, 범위가 10억처럼 큼, "최솟값의 최댓값" | **이분탐색** |

- DP는 배열을 만들어서 앞에서 구한 값을 재사용 (피보나치 수)
- 파이썬은 반복문이 느리므로, 큰 2차원 DP는 **1차원으로 압축**할 수 있는지 고민

```python
# 바로 앞 값만 쓰면 배열 대신 변수 두 개로
a, b = 0, 1
for _ in range(n):
    a, b = b, (a + b) % 1234567
```

---

## 3. 시간 초과 방지 팁

### ① 2차원 배열 초기화

```python
board = [[0] * M for _ in range(N)]   # O
board = [[0] * M] * N                 # X: 모든 행이 같은 리스트 (한 칸 바꾸면 그 열 전체가 바뀜)
```

### ② 문자열 합치기는 join

```python
# X: 반복문 안에서 += 를 계속하면 매번 새 문자열을 만들어 최악 O(N²)
result = ""
for c in arr:
    result += c

# O: 리스트에 모았다가 마지막에 한 번만 합치기, O(N)
parts = []
for c in arr:
    parts.append(c)
result = "".join(parts)

"".join(map(str, [1, 2, 3]))   # 숫자면 str로 바꿔서: "123"
```

### ③ 포함 여부 확인은 set / dict

| | `x in list` | `x in set` / `x in dict` |
|---|---|---|
| 시간 | O(N) | **O(1)** |

```python
seen = set(arr)        # 한 번만 만들어 두고
if x in seen:          # 반복해서 확인
```

- 반복문 안에서 `if x in 리스트`를 하면 전체가 O(N²) → 시간 초과
- 중복 제거도 `set`

### ④ 그 밖에

- 입력이 많으면 `input = sys.stdin.readline` (프로그래머스는 함수형이라 보통 필요 없음)
- 반복문 안에서 `max(리스트)`, `리스트.count()`, `sorted()`를 매번 호출하지 않기 (각각 O(N))

---

## 4. 문제 유형 판단표

| 문제에 보이는 말 | 먼저 떠올릴 것 |
|---|---|
| 최단거리, 최소 이동 횟수, 미로 | BFS + `deque` |
| 연결된 그룹 개수, 네트워크, 섬 | DFS/BFS + `visited`, 시작할 때마다 +1 |
| 모든 경우, 조합, 순서 | `itertools`, 재귀 DFS |
| 개수 세기, 이름 매칭, 중복 확인 | `dict`, `set` |
| 괄호, 직전 값과 비교해서 제거 | 스택 (`list`의 `append` / `pop` / `[-1]`) |
| 먼저 들어온 순서대로 처리 | 큐 (`deque`) |
| 가장 작은/큰 것을 계속 꺼내기 | `heapq` |
| 정렬 후 순서대로 고르기 | 그리디 |
| 앞의 결과로 다음 결과 계산 | DP |
| 입력 범위가 매우 큼 (10억) | 이분탐색 |
