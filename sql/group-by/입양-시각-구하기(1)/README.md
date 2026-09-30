# 입양 시각 구하기(1)

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59412
- 분류: GROUP BY
- 푼 날짜:
- 결과: 성공 (DATETIME 함수 검색)

## 핵심

- `HOUR(DATETIME)`으로 시(0~23)만 뽑아서 `GROUP BY`
- 09:00~19:59 → `BETWEEN 9 AND 19` (**양 끝 포함**)

## 막혔던 부분

- DATETIME에서 시간만 꺼내는 함수를 몰랐음

## 배운 점

- `YEAR()`, `MONTH()`, `DAY()`, `HOUR()`, `MINUTE()`로 날짜/시간의 일부를 꺼냄
- MySQL은 `GROUP BY`, `ORDER BY`에서 별칭(`HOUR`)을 바로 써도 됨
