# 없어진 기록 찾기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59042
- 분류: JOIN
- 푼 날짜:
- 결과: 성공

## 핵심

- 입양 기록(`ANIMAL_OUTS`)에는 있는데 보호 시작 기록(`ANIMAL_INS`)에는 없는 동물 찾기
- `ANIMAL_OUTS` 쪽을 전부 살리는 외부 조인 + `A.ANIMAL_ID IS NULL`
- "한쪽에만 있는 행 찾기" = **외부 조인 + IS NULL** 공식

## 막혔던 부분

## 배운 점

- `A RIGHT JOIN B`와 `B LEFT JOIN A`는 같은 결과
- 보통은 기준 테이블을 앞에 두는 `LEFT JOIN`을 더 많이 씀

```sql
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I
    ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;
```

- 다음 문제 "오랜 기간 보호한 동물(1)"은 이 문제의 반대 방향
