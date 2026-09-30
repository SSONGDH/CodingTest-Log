# Python 문법 정리

## 입출력 / 기본

## 리스트

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
