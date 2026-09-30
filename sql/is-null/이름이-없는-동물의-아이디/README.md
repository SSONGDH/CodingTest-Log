# 이름이 없는 동물의 아이디

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59039
- 분류: IS NULL
- 푼 날짜:
- 결과: 성공

## 핵심

- NULL 비교는 반드시 `IS NULL` / `IS NOT NULL`

## 막혔던 부분

## 배운 점

- `NAME = NULL`은 항상 참이 아니라서 결과가 0행이 됨 (NULL은 "값을 모름"이라 `=` 비교 불가)
- 문제에 정렬 조건이 있으면 `ORDER BY ANIMAL_ID` 붙이는 습관 들이기
