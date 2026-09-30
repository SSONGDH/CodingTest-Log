# DATETIME에서 DATE로 형 변환

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59414
- 분류: String, Date
- 푼 날짜:
- 결과: 성공 (DATE_FORMAT 검색)

## 핵심

- `DATE_FORMAT(DATETIME, '%Y-%m-%d')`: `2018-01-22 14:32:00` → `2018-01-22`

## 막혔던 부분

- 날짜 포맷 함수를 몰랐음

## 배운 점

| 기호 | 의미 | 예시 |
|---|---|---|
| `%Y` | 연도 4자리 | 2018 |
| `%y` | 연도 2자리 | 18 |
| `%m` | 월 2자리 | 01 |
| `%d` | 일 2자리 | 22 |
| `%H` | 시 (24시간) | 14 |
| `%i` | 분 | 32 (`%m`이 월이라 분은 `%i`) |

- `DATE(DATETIME)`도 날짜 부분만 꺼냄
