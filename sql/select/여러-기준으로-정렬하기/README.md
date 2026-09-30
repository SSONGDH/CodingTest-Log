# 여러 기준으로 정렬하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59404
- 분류: SELECT
- 푼 날짜:
- 결과: 성공

## 핵심

- `ORDER BY NAME ASC, DATETIME DESC`: 이름 오름차순, 이름이 같으면 날짜 내림차순
- 정렬 방향은 **컬럼마다 따로** 지정해야 함

## 막혔던 부분

## 배운 점

- `ORDER BY NAME, DATETIME DESC`에서 `DESC`는 `DATETIME`에만 적용되고 `NAME`은 기본값 `ASC`
