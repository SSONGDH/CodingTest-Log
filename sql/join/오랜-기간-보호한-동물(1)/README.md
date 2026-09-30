# 오랜 기간 보호한 동물(1)

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59044
- 분류: JOIN
- 푼 날짜:
- 결과: 성공 (LIMIT 검색)

## 핵심

- 아직 입양 안 간 동물 = `ANIMAL_INS`에는 있고 `ANIMAL_OUTS`에는 없음 → `LEFT JOIN` + `B.ANIMAL_ID IS NULL`
- 보호 시작일 오름차순으로 정렬해서 `LIMIT 3`으로 앞 3개만

## 막혔던 부분

- 상위 N개만 자르는 `LIMIT`을 몰랐음

## 배운 점

- "없어진 기록 찾기"와 방향만 반대인 같은 공식
- `LIMIT`은 항상 **맨 마지막**에 씀 (`ORDER BY` 다음)
- `LIMIT 5, 3`: 앞 5개를 건너뛰고 3개 (페이지 나누기)
