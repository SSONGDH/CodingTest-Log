# 문자열 내 p와 y의 개수

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12916
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 대문자/소문자를 각각 `count`해서 p 개수와 y 개수를 비교

## 막혔던 부분

## 다른 풀이에서 배운 점

- `lower()`로 먼저 소문자로 통일하면 대소문자를 따로 셀 필요가 없음
- 비교식 자체가 `True`/`False`라서 바로 `return` 가능

```python
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')
```
