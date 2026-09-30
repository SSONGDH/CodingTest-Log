# 동명 동물 수 찾기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59041
- 분류: GROUP BY
- 푼 날짜:
- 결과: 성공

## 핵심

- `GROUP BY NAME`으로 이름별로 묶고 `HAVING COUNT(NAME) >= 2`로 두 번 이상 쓰인 이름만 남김
- `WHERE`는 묶기 전 행 필터, `HAVING`은 묶은 뒤 그룹 필터

## 막혔던 부분

## 배운 점

- 이름이 없는 동물(NULL)도 하나의 그룹으로 묶이지만, `COUNT(NAME)`은 NULL을 세지 않아 0이 되므로 `HAVING`에서 자동으로 걸러짐
  - `COUNT(*)`를 쓰면 NULL 그룹이 남을 수 있어서 `WHERE NAME IS NOT NULL`이 필요함
- 테이블 별칭 `A`는 쓰지 않았으니 없어도 됨
