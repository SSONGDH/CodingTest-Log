# 고양이와 개는 몇 마리 있을까

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59040
- 분류: GROUP BY
- 푼 날짜:
- 결과: 성공

## 핵심

- `GROUP BY ANIMAL_TYPE`으로 종류별로 묶고 `COUNT(*)`로 개수 세기
- `ORDER BY ANIMAL_TYPE`: 알파벳순이라 Cat이 Dog보다 먼저 나옴

## 막혔던 부분

## 배운 점

- 결과 컬럼 이름을 지정하려면 `COUNT(*) AS count`
- `GROUP BY`를 쓰면 `SELECT`에는 묶은 컬럼과 집계 함수만 쓰기
