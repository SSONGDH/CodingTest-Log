# 프로세스

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 큐를 실제로 돌리지 않고, 리스트 위의 **현재 위치 `point`** 를 원형으로 이동시킴 (`point %= len`)
- 현재 값이 최댓값이면 실행(`pop`)하고 `count` 증가
- 실행한 위치가 `location`보다 앞이면 `location`을 한 칸 당김
- `location` 위치가 실행되면 종료

## 막혔던 부분

- 원소를 뺄 때 `location` 인덱스 보정이 헷갈림

## 다른 풀이에서 배운 점

- `deque`를 import했지만 실제로는 쓰지 않았음
- 큐 문제 정석: `(원래 인덱스, 우선순위)`를 같이 넣고 맨 앞을 꺼내서 뒤로 보내기
  - 인덱스 보정이 필요 없어서 실수가 줄어듦

```python
from collections import deque

def solution(priorities, location):
    q = deque((i, p) for i, p in enumerate(priorities))
    count = 0
    while q:
        cur = q.popleft()
        if any(cur[1] < p for _, p in q):
            q.append(cur)
        else:
            count += 1
            if cur[0] == location:
                return count
```
