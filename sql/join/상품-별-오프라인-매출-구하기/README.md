# 상품 별 오프라인 매출 구하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131533
- 분류: JOIN
- 푼 날짜:
- 결과: 성공

## 핵심

- 상품(`PRODUCT`)의 가격과 판매(`OFFLINE_SALE`)의 수량을 조인해서 곱함
- 상품 코드별로 `SUM(가격 * 수량)`, 매출 내림차순, 같으면 상품 코드 오름차순

## 막혔던 부분

## 배운 점

- 집계 함수 안에 계산식을 넣을 수 있음: `SUM(A.PRICE * B.SALES_AMOUNT)`
- 판매 기록마다 곱한 뒤 더하는 것과, 따로 더한 뒤 곱하는 것은 결과가 다름
