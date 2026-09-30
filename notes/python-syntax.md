# Python 문법 정리

## 입출력 / 기본

## 리스트

```python
arr[-1]                             # 마지막 원소 (arr[len(arr)-1]과 같음)
arr[-2]                             # 뒤에서 두 번째
if arr and arr[-1] == x:            # 빈 리스트면 arr[-1]에서 에러 → 먼저 비었는지 확인
```

```python
arr.sort()                          # 원본 정렬
sorted(arr, reverse=True)           # 새 리스트 반환
sorted(arr, key=lambda x: (x[1], -x[0]))  # 다중 조건 정렬
```

## 문자열

## 딕셔너리 / 집합

```python
from collections import defaultdict, Counter
d = defaultdict(int)
Counter("hello").most_common(1)     # [('l', 2)]
```

## collections / itertools / heapq

```python
from collections import deque
from itertools import combinations, permutations
import heapq
```

## 기타
