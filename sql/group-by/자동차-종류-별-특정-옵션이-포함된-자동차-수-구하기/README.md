# 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151137
- 분류: GROUP BY
- 푼 날짜:
- 결과: 성공

## 핵심

- `OPTIONS`에 통풍시트, 열선시트, 가죽시트 중 **하나라도 포함**된 차만 `WHERE`로 거름
- 그다음 `CAR_TYPE`별로 묶어서 `COUNT`, 종류 오름차순

## 막혔던 부분

- `LIKE`로 행을 거르려면 `WHERE`에 써야 한다는 점
- 여러 값을 찾을 때 `LIKE`를 **조건마다 따로** 쓰고 `OR`로 이어야 한다는 점

## 배운 점

```sql
WHERE OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%'   -- O
WHERE OPTIONS LIKE '%통풍시트%' OR '%열선시트%'                -- X
```

### IN을 쓰면 안 되는 이유

- `IN ('값1', '값2')`은 컬럼 값이 괄호 안의 값과 **정확히 일치**할 때만 찾음
- 이 문제의 `OPTIONS`는 `'열선시트,스마트키,주차감지센서'`처럼 여러 옵션이 쉼표로 이어진 문자열
- 그래서 `OPTIONS IN ('통풍시트', '열선시트')`는 옵션이 딱 하나만 있는 차가 아니면 못 찾음 → **일부 포함**을 찾는 `LIKE '%...%'`가 필요

| 상황 | 사용 |
|---|---|
| 값이 정확히 하나로 정해짐 (`CAR_TYPE = 'SUV'`) | `IN ('세단', 'SUV')` |
| 문자열 안에 포함됐는지 | `LIKE '%통풍시트%' OR LIKE ...` |

### 더 짧게 (MySQL)

```sql
WHERE OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
```

- `REGEXP`는 정규식으로, `|`는 "또는"
