# 성분으로 구분한 아이스크림 총 주문량

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133026
- 분류: GROUP BY
- 푼 날짜:
- 결과: 성공

## 핵심

- 주문 테이블(`FIRST_HALF`)과 성분 테이블(`ICECREAM_INFO`)을 `FLAVOR`로 `JOIN`
- 성분 타입별로 묶어서 `SUM(TOTAL_ORDER)`, 합계 오름차순

## 막혔던 부분

## 배운 점

- 별칭 `TOTAL_ORDER`가 원래 컬럼 이름과 같아서 `ORDER BY TOTAL_ORDER`가 무엇을 가리키는지 헷갈릴 수 있음
  - MySQL은 별칭(합계)을 우선해서 정답이 나왔지만, `ORDER BY SUM(TOTAL_ORDER)`처럼 명확하게 쓰는 게 안전
