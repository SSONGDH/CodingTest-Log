# SQL 문법 정리 (MySQL 기준)

## 실행 순서

`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`

## SELECT / 정렬

```sql
ORDER BY NAME ASC, DATETIME DESC   -- 정렬 방향은 컬럼마다 따로
LIMIT 3                            -- 맨 마지막에, 상위 3개만
```

## 집계

| 식 | 세는 대상 |
|---|---|
| `COUNT(*)` | 모든 행 (NULL 포함) |
| `COUNT(NAME)` | NAME이 NULL이 아닌 행 |
| `COUNT(DISTINCT NAME)` | NULL을 뺀 서로 다른 값 수 |

- 집계 함수 안에 계산식 가능: `SUM(PRICE * AMOUNT)`

## GROUP BY / HAVING

- `WHERE`: 그룹화 전 행 필터링
- `HAVING`: 그룹화 후 집계 결과 필터링
- `GROUP BY`를 쓰면 `SELECT`에는 묶은 컬럼과 집계 함수만

## JOIN

| 종류 | 설명 |
|---|---|
| `INNER JOIN` | 양쪽 모두 일치하는 행 |
| `LEFT JOIN` | 왼쪽 전체 + 오른쪽 일치 행 (없으면 NULL) |

- **한쪽에만 있는 행 찾기** = `LEFT JOIN` + `오른쪽.키 IS NULL`
- `A RIGHT JOIN B` == `B LEFT JOIN A`

## IS NULL

```sql
WHERE NAME IS NULL        -- NAME = NULL 은 항상 0행
IFNULL(col, '대체값')
COALESCE(col1, col2, '대체값')
```

## 조건 분기

```sql
CASE
    WHEN 조건1 THEN 값1
    WHEN 조건2 THEN 값2
    ELSE 기본값
END AS 별칭

IF(조건, 참일 때, 거짓일 때)   -- MySQL 전용, 분기 하나일 때
```

## 문자열

```sql
NAME LIKE '%EL%'    -- 포함 (MySQL은 대소문자 구분 안 함)
NAME LIKE 'EL%'     -- 시작
NAME LIKE '%EL'     -- 끝
NAME LIKE '_EL'     -- 아무 글자 1개 + EL

-- LIKE는 조건마다 컬럼을 다시 써야 함
COL LIKE 'A%' OR COL LIKE 'B%'

SUBSTRING(str, start, len)
```

- `AND`/`OR` 섞을 때는 괄호 필수 (`AND`가 먼저 계산됨)
- 문자열은 작은따옴표 `'...'`가 표준

## 날짜

```sql
YEAR(dt), MONTH(dt), DAY(dt), HOUR(dt), MINUTE(dt)
DATE(dt)                          -- 날짜 부분만
DATE_FORMAT(dt, '%Y-%m-%d')       -- %Y 연 %m 월 %d 일 %H 시 %i 분
DATEDIFF(end_date, start_date)    -- 일수 차이
```

- 월 범위 조건은 **다음 달 1일 미만**으로

```sql
WHERE dt >= '2022-05-01' AND dt < '2022-06-01'
```

  - `<= '2022-05-31'`은 5월 31일 00:00:00까지만 포함돼서 그날 기록이 빠짐
