# Python 문법 정리

## 목차

- [enumerate](#enumerate) · [sort / sorted](#sort--sorted) · [split / map](#split--map) · [zip](#zip)
- [음수 인덱스](#음수-인덱스--1) · [startswith](#startswith) · [dict.get](#dictget) · [deque](#deque)

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
- 쓴 문제: 기능개발, 프로세스
