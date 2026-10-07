# 카테고리 별 상품 개수 구하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131529
- 분류: String, Date
- 푼 날짜:
- 결과: 성공

## 핵심

- 상품 코드 앞 2자리가 카테고리 → `SUBSTR(PRODUCT_CODE, 1, 2)`
- 카테고리별로 묶어서 `COUNT`, 카테고리 오름차순

## 막혔던 부분

- `SUBSTR`, `LEFT` 사용법
- `GROUP BY`에서 `SELECT`의 별칭(`CATEGORY`)을 써도 되는지

## 배운 점

- `SUBSTR(문자열, 시작, 길이)`: **위치는 1부터**
- 앞부분만 자를 때는 `LEFT(PRODUCT_CODE, 2)`가 같은 결과로 더 짧음

```sql
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY,
       COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY;
```

- `GROUP BY CATEGORY`처럼 별칭을 쓰는 건 **MySQL만** 허용
  - 실행 순서상 `GROUP BY`가 `SELECT`보다 먼저지만, MySQL이 별칭을 미리 인식해 줌
  - 다른 DB에서는 `GROUP BY SUBSTR(PRODUCT_CODE, 1, 2)`처럼 식을 다시 써야 함
- 자세한 내용: `notes/sql-syntax.md`의 "별칭(AS)은 어디서 쓸 수 있나"
