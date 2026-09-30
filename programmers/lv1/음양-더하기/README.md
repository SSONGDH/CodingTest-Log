# 음양 더하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 인덱스 `i`로 `absolutes`와 `signs`를 같이 돌면서 `signs[i]`가 `False`면 빼고 `True`면 더함

## 막혔던 부분

## 다른 풀이에서 배운 점

- `zip`으로 두 리스트를 동시에 순회할 수 있음

```python
def solution(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))
```
