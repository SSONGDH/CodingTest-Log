# 최댓값과 최솟값

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12939
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: AI 풀이 참고 → 다시 풀기 필요

## 접근 방법

- `s.split()`으로 공백 기준 쪼개기 → 각각 `int`로 변환 → `min`, `max`
- f-string으로 `"최솟값 최댓값"` 형태로 반환

## 막혔던 부분

- AI 풀이를 참고함

## 다른 풀이에서 배운 점

- `map`을 안 쓰면 이렇게 쓸 수 있음

```python
def solution(s):
    numbers = []
    for x in s.split():
        numbers.append(int(x))
    return str(min(numbers)) + " " + str(max(numbers))
```

- `int("-3")`처럼 음수 문자열도 바로 변환됨
