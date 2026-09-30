# SQL 문법 정리 (MySQL 기준)

## 실행 순서

`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`

## SELECT

## GROUP BY / HAVING

- `WHERE`: 그룹화 전 행 필터링
- `HAVING`: 그룹화 후 집계 결과 필터링

## JOIN

| 종류 | 설명 |
|---|---|
| `INNER JOIN` | 양쪽 모두 일치하는 행 |
| `LEFT JOIN` | 왼쪽 전체 + 오른쪽 일치 행 (없으면 NULL) |

## IS NULL

```sql
IFNULL(col, '대체값')
COALESCE(col1, col2, '대체값')
```

## 문자열 / 날짜

```sql
DATE_FORMAT(date_col, '%Y-%m-%d')
YEAR(date_col), MONTH(date_col)
DATEDIFF(end_date, start_date)
SUBSTRING(str, start, len)
```
