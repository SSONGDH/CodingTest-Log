# 보호소에서 중성화한 동물

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59045
- 분류: JOIN
- 푼 날짜:
- 결과: 성공 (LIKE 사용법 검색)

## 핵심

- 들어올 때는 중성화 안 됨(`Intact`), 나갈 때는 중성화됨(`Spayed`/`Neutered`)
- 두 테이블을 `ANIMAL_ID`로 조인해서 들어올 때와 나갈 때 상태를 비교

## 막혔던 부분

- `LIKE`는 조건마다 따로 써야 한다는 걸 몰랐음

## 배운 점

- `LIKE 'Spayed%' OR 'Neutered%'`처럼 쓰면 안 되고, 컬럼을 매번 다시 써야 함

```sql
B.SEX_UPON_OUTCOME LIKE 'Spayed%' OR B.SEX_UPON_OUTCOME LIKE 'Neutered%'
```

- `AND`와 `OR`를 섞을 때는 **괄호 필수** (`AND`가 먼저 계산됨)
- 나갈 때 값은 `Intact`, `Spayed`, `Neutered` 셋 중 하나라서 `NOT LIKE 'Intact%'`로도 풀림
