# 폰켓몬

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공 (다른 표현 참고)

## 접근 방법

- 고를 수 있는 수는 `len(nums)//2`, 종류 수는 `len(set(nums))`
- 둘 중 작은 값이 정답

## 막혔던 부분

- 더 짧은 표현이 있는지 다른 풀이를 참고함

## 다른 풀이에서 배운 점

- `len(set(...))`은 `list`로 바꾸지 않아도 바로 쓸 수 있음
- 조건 표현식 대신 `min`으로 한 줄 정리

```python
def solution(nums):
    return min(len(nums) // 2, len(set(nums)))
```
