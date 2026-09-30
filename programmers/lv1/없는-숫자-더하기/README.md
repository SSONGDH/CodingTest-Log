# 없는 숫자 더하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 1~9를 돌면서 `numbers.count(i)`가 0인 숫자만 더함

## 막혔던 부분

## 다른 풀이에서 배운 점

- 존재 여부는 `count` 대신 `in` / `not in`으로 확인하는 게 더 직관적

```python
if i not in numbers:
    answer += i
```

- 0~9 합은 45라서 `45 - sum(numbers)` 한 줄로도 풀림
