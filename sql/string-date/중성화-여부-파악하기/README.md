# 중성화 여부 파악하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59409
- 분류: String, Date
- 푼 날짜:
- 결과: 성공 (IF/CASE 검색)

## 핵심

- `CASE WHEN 조건 THEN 값 ELSE 값 END`: SQL의 if-else
- `Neutered`나 `Spayed`가 들어 있으면 `'O'`, 아니면 `'X'`

## 막혔던 부분

- IF, CASE 문법을 몰랐음

## 배운 점

- 조건이 하나면 `IF(조건, 참일 때, 거짓일 때)`로 더 짧게 쓸 수 있음 (MySQL 전용)

```sql
IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS 중성화
```

- 분기가 여러 개면 `CASE`에 `WHEN`을 여러 줄 씀
