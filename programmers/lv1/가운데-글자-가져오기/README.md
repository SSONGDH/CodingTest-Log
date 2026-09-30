# 가운데 글자 가져오기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 길이가 짝수면 `len(s)//2-1`, `len(s)//2` 두 글자, 홀수면 `len(s)//2` 한 글자

## 막혔던 부분

## 다른 풀이에서 배운 점

- 슬라이싱으로 짝수/홀수를 한 번에 처리할 수 있음

```python
def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]
```
