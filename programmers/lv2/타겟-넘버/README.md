# 타겟 넘버

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: AI 풀이 참고 → 재귀 DFS로 다시 풀기 필요

## 접근 방법

- 숫자마다 `+` 또는 `-` 두 가지 → 모든 경우의 합을 만들어 보고 `target`과 같은 개수를 셈
- `result`에 "지금까지 만들 수 있는 합"을 전부 들고 있다가, 숫자 하나를 꺼낼 때마다 각 합에 `+숫자`, `-숫자`를 붙여 두 배로 늘림
- 한 단계(숫자 하나)씩 전부 펼치는 방식이라 **BFS와 같은 흐름**

`numbers = [1, 2]`일 때 (`pop()`이라 뒤에서부터 꺼냄)

| 꺼낸 숫자 | result |
|---|---|
| 시작 | `[0]` |
| 2 | `[2, -2]` |
| 1 | `[3, 1, -1, -3]` |

## 막혔던 부분

- AI 풀이를 참고함
- 재귀(DFS)로 풀고 싶었는데 어려워서 리스트를 단계별로 늘리는 방식으로 풀었음

## 다른 풀이에서 배운 점

### 1. 재귀 DFS 풀이

```python
def solution(numbers, target):
    def dfs(i, total):
        if i == len(numbers):                  # ① 숫자를 다 썼으면
            return 1 if total == target else 0 #    target이면 1가지, 아니면 0
        return (dfs(i + 1, total + numbers[i]) # ② 지금 숫자를 더하는 경우
              + dfs(i + 1, total - numbers[i]))#    빼는 경우, 두 결과를 합침

    return dfs(0, 0)                           # 0번 숫자부터, 합 0으로 시작
```

**재귀 함수 만드는 순서**

1. **함수가 들고 다닐 정보 정하기**: "몇 번째 숫자를 볼 차례인지(`i`)", "지금까지의 합(`total`)"
2. **끝나는 조건(종료 조건) 먼저 쓰기**: 숫자를 다 썼을 때(`i == len(numbers)`) 답이 되는지 판단해서 반환
3. **다음 단계로 넘기기**: 지금 할 수 있는 선택(+, -)마다 `i + 1`로 자기 자신을 다시 부름
4. **결과 합치기**: 두 선택에서 돌아온 개수를 더해서 반환

**호출 흐름** (`numbers = [1, 2]`, `target = 1`)

```
dfs(0, 0)
├── +1 → dfs(1, 1)
│        ├── +2 → dfs(2, 3)   다 씀, 3 ≠ 1 → 0
│        └── -2 → dfs(2, -1)  다 씀, -1 ≠ 1 → 0
└── -1 → dfs(1, -1)
         ├── +2 → dfs(2, 1)   다 씀, 1 == 1 → 1
         └── -2 → dfs(2, -3)  다 씀, -3 ≠ 1 → 0
```

- 아래에서부터 더해 올라옴: `0 + 0` → 0, `1 + 0` → 1, 맨 위 `0 + 1` = **1**
- 한 갈래를 끝까지 내려갔다가 돌아와서 다음 갈래로 가는 것이 **DFS(깊이 우선 탐색)**
- 종료 조건이 없으면 끝없이 호출돼서 `RecursionError`

**전역 변수로 개수를 세는 방식** (반환값 합치기가 헷갈리면 이쪽이 더 직관적)

```python
def solution(numbers, target):
    answer = 0

    def dfs(i, total):
        nonlocal answer                 # 바깥 함수의 answer를 수정하겠다는 선언
        if i == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total - numbers[i])

    dfs(0, 0)
    return answer
```

### 2. 큐(deque) BFS 풀이

내 풀이를 실제 큐로 바꾸면 이런 모양. `(다음 볼 인덱스, 지금까지의 합)`을 큐에 넣음

```python
from collections import deque

def solution(numbers, target):
    q = deque([(0, 0)])
    answer = 0
    while q:
        i, total = q.popleft()
        if i == len(numbers):
            if total == target:
                answer += 1
            continue
        q.append((i + 1, total + numbers[i]))
        q.append((i + 1, total - numbers[i]))
    return answer
```

### 3. itertools.product 풀이

```python
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
```

`numbers = [1, 2]`로 한 줄씩 보면

**① 숫자마다 (+, -) 쌍 만들기**

```python
l = [(x, -x) for x in numbers]
# [(1, -1), (2, -2)]
```

**② `*l`로 리스트 풀어서 넘기기 (언패킹)**

```python
product(*l)
# product((1, -1), (2, -2)) 와 같음
```

- `*`는 리스트 안의 원소를 하나씩 꺼내서 각각 따로 넘겨줌

**③ `product`: 각 묶음에서 하나씩 골라 만들 수 있는 모든 조합**

```python
list(product((1, -1), (2, -2)))
# [(1, 2), (1, -2), (-1, 2), (-1, -2)]
```

- 이중 for문과 같은 뜻 (묶음이 n개면 n중 for문)

```python
for a in (1, -1):
    for b in (2, -2):
        (a, b)
```

**④ `map(sum, ...)`: 조합마다 합 구하기**

```python
list(map(sum, product(*l)))
# [3, -1, 1, -3]
```

**⑤ target 개수 세기**

```python
[3, -1, 1, -3].count(1)   # 1
```

### 정리

| 풀이 | 특징 |
|---|---|
| 내 풀이 (단계별 리스트) | BFS와 같은 흐름, 모든 합을 메모리에 들고 있음 |
| 재귀 DFS | 코테 정석, 백트래킹/조합 문제로 확장됨 → **꼭 다시 쳐보기** |
| 큐 BFS | 최단거리 문제(게임 맵 최단거리)의 뼈대 |
| product | 가장 짧지만 원리를 알고 써야 함 |

- 숫자 n개면 경우의 수 2ⁿ개. 이 문제는 n ≤ 20이라 약 100만 개로 완전탐색 가능
- 내 풀이의 `numbers.pop()`은 입력 리스트를 비워버림. 함수 밖에서 다시 쓸 일이 있으면 `for x in numbers:`로 도는 게 안전
