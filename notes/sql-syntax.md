# SQL 문법 정리 (MySQL 기준)

## 목차

- [실행 순서](#실행-순서) · [WHERE vs HAVING](#where-vs-having) · [집계](#집계) · [JOIN](#join)
- [IS NULL](#is-null) · [IF / CASE](#if--case) · [LIKE](#like) · [문자열 자르기 / SUBSTR, LEFT](#문자열-자르기--substr-left)
- [날짜 / DATE_FORMAT](#날짜--date_format) · [정렬 / LIMIT](#정렬--limit) · [별칭(AS)은 어디서 쓸 수 있나](#별칭as은-어디서-쓸-수-있나)

---

## 실행 순서

`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`

- 이 순서를 알면 WHERE/HAVING 차이, 별칭을 어디서 쓸 수 있는지가 전부 설명됨

---

## 별칭(AS)은 어디서 쓸 수 있나

```sql
SELECT SUBSTR(PRODUCT_CODE, 1, 2) AS CATEGORY,
       COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY          -- SELECT의 별칭을 GROUP BY에서 사용
ORDER BY CATEGORY;
```

| 절 | 별칭 사용 | 이유 |
|---|---|---|
| `WHERE` | **불가** | `SELECT`보다 먼저 실행돼서 별칭이 아직 없음 |
| `GROUP BY` | MySQL만 가능 | 표준 SQL 순서상 불가지만 MySQL이 예외적으로 허용 |
| `HAVING` | MySQL만 가능 | 위와 같음 |
| `ORDER BY` | **가능** (모든 DB) | `SELECT` 다음에 실행되므로 별칭이 이미 있음 |

**MySQL의 예외적 허용**

- 실행 순서로 보면 `GROUP BY`, `HAVING`은 `SELECT`보다 먼저라서 별칭을 모르는 게 정상
- MySQL은 편의를 위해 쿼리를 해석할 때 `SELECT`의 별칭을 미리 인식해서 `GROUP BY`, `HAVING`에서도 쓸 수 있게 해 줌
- Oracle 등 다른 DB에서는 에러 → 별칭 대신 **식을 그대로** 다시 써야 함

```sql
GROUP BY SUBSTR(PRODUCT_CODE, 1, 2)   -- 모든 DB에서 동작
```

- `WHERE CATEGORY = 'A1'`은 MySQL에서도 에러 → `WHERE SUBSTR(PRODUCT_CODE, 1, 2) = 'A1'`
- 쓴 문제: 카테고리 별 상품 개수 구하기, 입양 시각 구하기(1)

---

## WHERE vs HAVING

| | `WHERE` | `HAVING` |
|---|---|---|
| 시점 | `GROUP BY` **전** (묶기 전) | `GROUP BY` **후** (묶은 뒤) |
| 거르는 대상 | 행 하나하나 | 묶인 그룹 |
| 집계 함수(`COUNT`, `SUM`) | 사용 불가 | 사용 가능 |

```sql
SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL        -- ① 묶기 전: 이름 없는 행 제거
GROUP BY NAME                 -- ② 이름별로 묶기
HAVING COUNT(*) >= 2          -- ③ 묶은 뒤: 2마리 이상인 그룹만
ORDER BY NAME;
```

- 판단법: **조건에 `COUNT`, `SUM`, `MAX` 같은 집계가 들어가면 `HAVING`**, 아니면 `WHERE`
- `WHERE COUNT(*) >= 2`는 에러 (묶기 전이라 개수를 아직 모름)
- 쓴 문제: 동명 동물 수 찾기

---

## 집계

| 식 | 세는 대상 |
|---|---|
| `COUNT(*)` | 모든 행 (NULL 포함) |
| `COUNT(NAME)` | NAME이 NULL이 아닌 행 |
| `COUNT(DISTINCT NAME)` | NULL을 뺀 서로 다른 값 수 |

- `SUM`, `AVG`, `MAX`, `MIN`
- 집계 함수 안에 계산식 가능: `SUM(PRICE * SALES_AMOUNT)`
- `GROUP BY`를 쓰면 `SELECT`에는 **묶은 컬럼과 집계 함수만**

---

## JOIN

| 종류 | 결과 |
|---|---|
| `INNER JOIN` (= `JOIN`) | 양쪽 모두 일치하는 행 |
| `LEFT JOIN` | 왼쪽 전체 + 오른쪽 일치 행 (없으면 NULL) |

```sql
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
  ON A.ANIMAL_ID = B.ANIMAL_ID
```

- **한쪽에만 있는 행 찾기** = `LEFT JOIN` + `오른쪽.키 IS NULL`
  - 없어진 기록 찾기 (OUTS에만 있음), 오랜 기간 보호한 동물(1) (INS에만 있음)
- `A RIGHT JOIN B` == `B LEFT JOIN A`
- 두 테이블에 같은 컬럼명이 있으면 `A.`, `B.`처럼 별칭 필수

---

## IS NULL

```sql
WHERE NAME IS NULL          -- NAME = NULL 은 항상 0행
WHERE NAME IS NOT NULL
IFNULL(NAME, 'No name')     -- NULL이면 대체값
COALESCE(col1, col2, '기본')-- 처음으로 NULL이 아닌 값
```

---

## IF / CASE

SQL에서 if-else를 쓰는 방법. **`SELECT`에서 값을 바꿔 보여줄 때** 사용

**`IF(조건, 참일 때, 거짓일 때)`**: 분기가 2개일 때 (MySQL 전용)

```sql
SELECT ANIMAL_ID,
       IF(SEX_UPON_INTAKE LIKE '%Neutered%'
          OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS 중성화
FROM ANIMAL_INS;
```

**`CASE WHEN ... END`**: 분기가 여러 개일 때 (모든 DB 공통)

```sql
SELECT ANIMAL_ID,
       CASE
           WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN '수컷 중성화'
           WHEN SEX_UPON_INTAKE LIKE '%Spayed%'   THEN '암컷 중성화'
           ELSE '중성화 안 됨'
       END AS 상태
FROM ANIMAL_INS;
```

- 위에서부터 검사해서 **처음 맞는 `WHEN`** 의 값을 씀
- `ELSE`를 빼면 아무것도 안 맞을 때 NULL
- `END` 빼먹기 쉬움
- 쓴 문제: 중성화 여부 파악하기

---

## LIKE

| 패턴 | 의미 |
|---|---|
| `'%EL%'` | EL 포함 |
| `'EL%'` | EL로 시작 |
| `'%EL'` | EL로 끝 |
| `'_EL'` | 아무 글자 1개 + EL |

```sql
-- 조건마다 컬럼을 다시 써야 함
COL LIKE 'Spayed%' OR COL LIKE 'Neutered%'     -- O
COL LIKE 'Spayed%' OR 'Neutered%'              -- X
```

- MySQL은 기본적으로 대소문자 구분 안 함
- `AND`/`OR` 섞을 때는 **괄호 필수** (`AND`가 먼저 계산됨)
- `%`가 없는 `LIKE '경제'`는 `= '경제'`와 같음
- 문자열은 작은따옴표 `'...'`가 표준

---

## 문자열 자르기 / SUBSTR, LEFT

**`SUBSTR(문자열, 시작 위치, 길이)`**: 시작 위치부터 길이만큼 자르기

```sql
SUBSTR('A1000011', 1, 2)    -- 'A1'      1번째부터 2글자
SUBSTR('A1000011', 3, 4)    -- '0000'    3번째부터 4글자
SUBSTR('A1000011', 3)       -- '000011'  길이 생략 → 끝까지
SUBSTR('A1000011', -2)      -- '11'      음수 → 뒤에서 2번째부터 끝까지
```

- **위치는 1부터 시작** (파이썬은 0부터라 헷갈림 주의)
- `SUBSTRING()`도 완전히 같은 함수

**`LEFT(문자열, 길이)` / `RIGHT(문자열, 길이)`**: 앞/뒤에서 길이만큼

```sql
LEFT('A1000011', 2)     -- 'A1'   앞에서 2글자
RIGHT('A1000011', 2)    -- '11'   뒤에서 2글자
```

- 앞부분만 필요하면 `LEFT(col, 2)` == `SUBSTR(col, 1, 2)` → 더 짧고 읽기 쉬움
- 중간을 잘라야 하면 `SUBSTR`

| 하고 싶은 것 | 함수 |
|---|---|
| 앞 n글자 | `LEFT(col, n)` 또는 `SUBSTR(col, 1, n)` |
| 뒤 n글자 | `RIGHT(col, n)` 또는 `SUBSTR(col, -n)` |
| k번째부터 n글자 | `SUBSTR(col, k, n)` |

**파이썬 슬라이싱과 비교**

| SQL | Python |
|---|---|
| `SUBSTR(s, 1, 2)` | `s[0:2]` |
| `SUBSTR(s, 3, 4)` | `s[2:6]` |
| `LEFT(s, 2)` | `s[:2]` |
| `RIGHT(s, 2)` | `s[-2:]` |

**기타 문자열 함수**

```sql
LENGTH('abc')            -- 3   (한글은 바이트 수라 CHAR_LENGTH 사용)
CONCAT('A', '-', 'B')    -- 'A-B'
REPLACE('a-b', '-', '')  -- 'ab'
UPPER('ab'), LOWER('AB')
```

- 쓴 문제: 카테고리 별 상품 개수 구하기

---

## 날짜 / DATE_FORMAT

**일부만 꺼내기**

```sql
YEAR(DATETIME)     -- 2018
MONTH(DATETIME)    -- 1
DAY(DATETIME)      -- 22
HOUR(DATETIME)     -- 14   (입양 시각 구하기)
DATE(DATETIME)     -- 2018-01-22
```

**`DATE_FORMAT(날짜, '형식')`**: 원하는 모양의 문자열로

```sql
DATE_FORMAT(DATETIME, '%Y-%m-%d')   -- 2018-01-22
DATE_FORMAT(DATETIME, '%Y-%m')      -- 2018-01
DATE_FORMAT(DATETIME, '%H:%i')      -- 14:32
```

| 기호 | 의미 | 예시 |
|---|---|---|
| `%Y` | 연도 4자리 | 2018 |
| `%y` | 연도 2자리 | 18 |
| `%m` | 월 (2자리) | 01 |
| `%d` | 일 (2자리) | 22 |
| `%H` | 시 (24시간) | 14 |
| `%i` | 분 | 32 |
| `%s` | 초 | 00 |

- **월은 `%m`, 분은 `%i`** (헷갈리기 쉬움)
- `Y`는 대문자, 나머지 `m`, `d`는 소문자

**날짜 범위 조건**

```sql
WHERE DT >= '2022-05-01' AND DT < '2022-06-01'      -- 5월 전체 (안전)
WHERE DATE_FORMAT(DT, '%Y-%m') = '2022-05'          -- 같은 결과
WHERE YEAR(DT) = 2022 AND MONTH(DT) = 5             -- 같은 결과
```

- `<= '2022-05-31'`은 5월 31일 00:00:00까지만 포함돼서 그날 기록이 빠짐
- `DATEDIFF(끝, 시작)`: 일수 차이
- 쓴 문제: 입양 시각 구하기(1), 진료과별 총 예약 횟수, DATETIME에서 DATE로 형 변환

---

## 정렬 / LIMIT

```sql
ORDER BY NAME ASC, DATETIME DESC   -- 정렬 방향은 컬럼마다 따로 (기본 ASC)
LIMIT 3                            -- 상위 3개만, 항상 맨 마지막
LIMIT 5, 3                         -- 5개 건너뛰고 3개
```

- 가장 큰 값 **한 행 전체**가 필요하면 `ORDER BY ... DESC LIMIT 1`
