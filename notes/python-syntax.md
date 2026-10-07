# Python 문법 정리

## 목차

- [enumerate](#enumerate) · [sort / sorted](#sort--sorted) · [split / map](#split--map) · [zip](#zip)
- [음수 인덱스](#음수-인덱스--1) · [startswith](#startswith) · [dict.get](#dictget) · [deque](#deque)
- [2차원 리스트](#2차원-리스트) · [* 언패킹 / itertools.product](#-언패킹--itertoolsproduct)

---

## enumerate

반복하면서 **인덱스와 값을 같이** 꺼냄

```python
fruits = ['a', 'b', 'c']

for i, v in enumerate(fruits):
    print(i, v)       # 0 a / 1 b / 2 c

for i, v in enumerate(fruits, 1):   # 인덱스를 1부터 시작
    print(i, v)       # 1 a / 2 b / 3 c
```

- `for i in range(len(arr)):` + `arr[i]`를 한 번에 쓰는 것과 같음
- 쓴 문제: 두 개 뽑아서 더하기, 모의고사, 완주하지 못한 선수

---

## sort / sorted

| | `arr.sort()` | `sorted(arr)` |
|---|---|---|
| 원본 | **바뀜** | 안 바뀜 |
| 반환값 | `None` | 정렬된 새 리스트 |
| 대상 | 리스트만 | 문자열, set, dict 등 전부 |

```python
arr = [3, 1, 2]
arr.sort()                    # arr → [1, 2, 3]
new = sorted(arr, reverse=True)   # [3, 2, 1], arr는 그대로

sorted("cba")                 # ['a', 'b', 'c']
sorted({3, 1, 2})             # [1, 2, 3]  set → 리스트
```

**정렬 기준 바꾸기 (`key`)**

```python
words = ["bb", "a", "ccc"]
sorted(words, key=len)                    # 길이순 ['a', 'bb', 'ccc']

pairs = [(1, 'b'), (2, 'a'), (1, 'a')]
sorted(pairs, key=lambda x: x[1])         # 두 번째 값 기준
sorted(pairs, key=lambda x: (x[0], x[1])) # 첫 번째 → 같으면 두 번째
sorted(pairs, key=lambda x: (-x[0], x[1]))# 첫 번째 내림차순, 두 번째 오름차순
```

- 주의: `answer = arr.sort()`라고 쓰면 `answer`는 `None`
- 문자열 정렬은 사전순: `"119" < "1195524421" < "97674223"` (전화번호 목록 핵심)
- 쓴 문제: K번째수, 완주하지 못한 선수, 전화번호 목록

---

## split / map

**`split()`**: 문자열을 쪼개서 리스트로

```python
"1 2 -3".split()        # ['1', '2', '-3']   공백 기준 (여러 칸 공백도 처리)
"a,b,c".split(",")      # ['a', 'b', 'c']    구분자 지정
```

**`map(함수, 반복 가능한 것)`**: 모든 원소에 함수를 적용

```python
numbers = list(map(int, "1 2 -3".split()))   # [1, 2, -3]
```

- `map`의 결과는 리스트가 아니라서 `list()`로 감싸야 인덱싱 가능
- 아래 반복문과 같은 뜻

```python
numbers = []
for x in "1 2 -3".split():
    numbers.append(int(x))
```

- 쓴 문제: 최댓값과 최솟값

---

## zip

여러 리스트를 **같은 위치끼리 묶어서** 동시에 순회

```python
names = ['a', 'b', 'c']
scores = [90, 80, 70]

for n, s in zip(names, scores):
    print(n, s)       # a 90 / b 80 / c 70

list(zip(names, scores))   # [('a', 90), ('b', 80), ('c', 70)]
dict(zip(names, scores))   # {'a': 90, 'b': 80, 'c': 70}
```

- 길이가 다르면 **짧은 쪽에 맞춰** 끝남
- `for i in range(len(a)):` + `a[i]`, `b[i]` 대신 쓸 수 있음
- 쓸 수 있는 문제: 음양 더하기, 기능개발

---

## 음수 인덱스 (-1)

```python
arr = ['b', 'a', 'c']
arr[-1]      # 'c'  맨 뒤
arr[-2]      # 'a'  뒤에서 두 번째
arr[:-1]     # ['b', 'a']  마지막 빼고
arr[::-1]    # ['c', 'a', 'b']  뒤집기
```

- 스택 맨 위 확인: `stack[-1]`
- 빈 리스트에서 `arr[-1]`은 에러 → `if arr and arr[-1] == x:`처럼 먼저 확인
- 쓴 문제: 같은 숫자는 싫어, 짝지어 제거하기

---

## startswith

문자열이 특정 문자열로 **시작하는지** `True`/`False`

```python
"1195524421".startswith("119")   # True
"97674223".startswith("119")     # False
"hello".endswith("lo")           # True   끝나는지
```

- 슬라이싱으로 쓰면: `b[:len(a)] == a`
- 쓴 문제: 전화번호 목록

---

## dict.get

`d.get(키, 기본값)`: 키가 있으면 값, **없으면 기본값** (에러 안 남)

```python
d = {'a': 1}
d['b']            # KeyError
d.get('b')        # None
d.get('b', 0)     # 0
```

**개수 세기 공식** (해시 문제 뼈대)

```python
count = {}
for x in ['a', 'b', 'a']:
    count[x] = count.get(x, 0) + 1
# {'a': 2, 'b': 1}
```

- 처음 보는 키면 `0 + 1`, 이미 있으면 `기존값 + 1`
- 같은 결과를 내는 다른 방법

```python
from collections import Counter
Counter(['a', 'b', 'a'])          # Counter({'a': 2, 'b': 1})
```

**딕셔너리 순회**

```python
for k in d:              # 키
for v in d.values():     # 값
for k, v in d.items():   # 키, 값 같이
```

- 쓴 문제: 완주하지 못한 선수(딕셔너리 풀이), 의상

---

## deque

양쪽 끝에서 넣고 빼기가 빠른 자료구조. **큐 문제는 무조건 이거**

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)        # 오른쪽에 넣기  [1, 2, 3, 4]
q.popleft()        # 왼쪽에서 빼기  1 반환, [2, 3, 4]
q.appendleft(0)    # 왼쪽에 넣기    [0, 2, 3, 4]
q.pop()            # 오른쪽에서 빼기 4 반환
q[0]               # 맨 앞 확인 (빼지 않음)
len(q)             # 길이
while q:           # 빌 때까지 반복
```

| | 리스트 `pop(0)` | deque `popleft()` |
|---|---|---|
| 속도 | O(N), 뒤 원소를 전부 당김 | O(1) |

- 스택(뒤에서 넣고 뒤에서 빼기)은 그냥 리스트 `append` / `pop`으로 충분
- 큐(뒤에서 넣고 앞에서 빼기)는 `deque`

### 괄호 언제 뭘 쓰나 (헷갈림 주의)

**만들 때 `deque([...])`: 대괄호 필요**

`deque()`는 "여러 개가 든 묶음"을 받아서 **안의 원소를 하나씩** 꺼내 넣음

```python
deque([(0, 0, 1)])   # [(0, 0, 1)]   → 튜플 1개가 든 큐  O
deque((0, 0, 1))     # [0, 0, 1]     → 숫자 3개로 쪼개짐  X
deque([1, 2, 3])     # [1, 2, 3]     → 숫자 3개
deque()              # 빈 큐
```

- 시작 원소가 튜플 하나라면 **리스트로 한 번 감싸서** `[(0, 0, 1)]`

**넣을 때 `append((...))`: 대괄호 쓰면 안 됨**

`append()`는 받은 것 **하나를 그대로** 넣음

```python
q.append((nx, ny, d))    # 튜플 1개 들어감               O
q.append([(nx, ny, d)])  # 리스트 1개가 통째로 들어감     X
q.append(nx, ny, d)      # TypeError: 인자는 1개만 받음   X
```

- 소괄호가 **두 겹**: 바깥은 함수 호출, 안쪽은 튜플
- 여러 개를 한 번에 넣으려면 `q.extend([a, b, c])`

| | 받는 것 | 동작 |
|---|---|---|
| `deque(묶음)` | 리스트 등 | 안의 원소를 **하나씩** 넣음 |
| `q.append(x)` | 아무거나 1개 | `x` **그대로** 넣음 |
| `q.extend(묶음)` | 리스트 등 | 안의 원소를 **하나씩** 넣음 |

**꺼낼 때 언패킹**

```python
x, y, d = q.popleft()    # 넣은 튜플이 (x, y, d) 3개짜리여야 함
```

- `ValueError: not enough values to unpack (expected 3, got 1)`
  → 꺼낸 값이 3개짜리 튜플이 아니라 1개짜리 (보통 `append`할 때 괄호 실수)
- 쓴 문제: 기능개발, 프로세스, 타겟 넘버, 게임 맵 최단거리

---

## 2차원 리스트

**만들기**

```python
n, m = 3, 4                                  # 3행 4열
visited = [[False] * m for _ in range(n)]    # O
visited = [[False] * m] * n                  # X: 모든 행이 같은 리스트를 가리킴
```

```python
a = [[0] * 3] * 2
a[0][0] = 9
print(a)    # [[9, 0, 0], [9, 0, 0]]  ← 한 줄만 바꿨는데 전부 바뀜
```

**인덱스: `maps[행][열]`**

```python
maps = [[1, 0, 1],
        [1, 1, 1]]
len(maps)       # 2  행 개수 (세로 길이)
len(maps[0])    # 3  열 개수 (가로 길이)
maps[1][2]      # 1  1번 행, 2번 열
```

- 행 = 세로 위치 = `y` = `r`, 열 = 가로 위치 = `x` = `c` → **`maps[y][x]`**, `maps[r][c]`
- `x`, `y`가 헷갈리면 처음부터 `r`, `c`로 이름 짓기
- 범위 검사: `0 <= r < len(maps) and 0 <= c < len(maps[0])` (**`-1` 붙이지 않음**)
- 범위 검사를 **먼저**, 그 다음 `maps[r][c]` 확인 (반대로 하면 IndexError)

**상하좌우 이동**

```python
for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    nr, nc = r + dr, c + dc
```

- 쓴 문제: 게임 맵 최단거리

---

## * 언패킹 / itertools.product

**`*`**: 리스트 안의 원소를 하나씩 꺼내서 따로따로 넘김

```python
l = [(1, -1), (2, -2)]
print(*l)            # (1, -1) (2, -2)
f(*l)                # f((1, -1), (2, -2)) 와 같음
```

### product 사용법

각 묶음에서 **하나씩** 골라 만들 수 있는 **모든 조합**. n중 for문을 한 줄로 쓰는 것

**① 기본: 묶음을 여러 개 넘기기**

```python
from itertools import product

list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

- 아래 이중 for문과 같음 (앞 묶음이 바깥 반복)

```python
for x in [1, 2]:
    for y in ['a', 'b']:
        (x, y)
```

- 결과 개수 = 각 묶음 길이의 곱 (2 × 2 = 4)
- 결과는 **튜플**이고, `product(...)` 자체는 리스트가 아니라서 출력하려면 `list()`로 감싸기
  - `for`로 돌 때는 `list()` 없이 바로 써도 됨

**② `repeat`: 같은 묶음을 여러 번**

```python
list(product([0, 1], repeat=3))
# [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]

list(product('AB', repeat=2))
# [('A','A'), ('A','B'), ('B','A'), ('B','B')]
```

- `product([0, 1], [0, 1], [0, 1])`과 같음
- 문자열도 글자 하나씩 묶음으로 취급

**③ 묶음 개수가 정해져 있지 않을 때: 리스트 만들고 `*`로 풀기**

```python
numbers = [4, 1, 2, 1]
l = [(x, -x) for x in numbers]   # [(4,-4), (1,-1), (2,-2), (1,-1)]
product(*l)                      # product((4,-4), (1,-1), (2,-2), (1,-1))
```

- `product(l)`로 쓰면 리스트 하나만 넘긴 것이라 원하는 결과가 안 나옴 → **`*` 필수**

**④ 조합마다 계산하기**

```python
for combo in product(*l):
    total = sum(combo)          # (4, -1, 2, -1) → 4

sums = list(map(sum, product(*l)))   # 모든 합을 한 번에
sums = [sum(c) for c in product(*l)] # 같은 뜻 (리스트 컴프리헨션)
```

**⑤ 코테에서 자주 쓰는 형태**

```python
# 숫자마다 + 또는 - (타겟 넘버)
product(*[(x, -x) for x in numbers])

# 각 자리에 올 수 있는 글자 전부 (모음 사전류)
product('AEIOU', repeat=5)

# 켜기/끄기 모든 경우 (부분집합)
for bits in product([0, 1], repeat=len(arr)):
    chosen = [arr[i] for i in range(len(arr)) if bits[i]]

# 이중 for문 대신 좌표 전부 돌기
for r, c in product(range(n), range(m)):
    grid[r][c]
```

**주의**

- 경우의 수가 곱으로 늘어남: `(+, -)` 20개면 2²⁰ ≈ 100만 개 (가능), 30개면 약 10억 개 (시간 초과)
- `list()`로 감싸면 전부 메모리에 올라가니, 개수가 많으면 `for`로 바로 돌기

**itertools 비교** (`[1, 2, 3]`에서 2개)

| 함수 | 의미 | 개수 |
|---|---|---|
| `product(arr, repeat=2)` | 중복 허용, 순서 있음 | 9 |
| `permutations(arr, 2)` | 순열: 중복 X, 순서 있음 | 6 |
| `combinations(arr, 2)` | 조합: 중복 X, 순서 없음 | 3 |

- 쓴 문제: 타겟 넘버 (product), 두 개 뽑아서 더하기 (combinations로도 가능)
