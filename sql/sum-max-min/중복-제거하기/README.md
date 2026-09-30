# 중복 제거하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59408
- 분류: SUM, MAX, MIN
- 푼 날짜:
- 결과: 성공

## 핵심

- `COUNT(DISTINCT NAME)`: 중복을 뺀 이름 종류 수

## 막혔던 부분

## 배운 점

| 식 | 세는 대상 |
|---|---|
| `COUNT(*)` | 모든 행 (NULL 포함) |
| `COUNT(NAME)` | NAME이 NULL이 아닌 행 |
| `COUNT(DISTINCT NAME)` | NULL을 뺀 서로 다른 이름 수 |

- 문제의 "이름이 NULL인 경우는 집계하지 않는다"는 조건을 `COUNT(DISTINCT NAME)`이 자동으로 처리함
