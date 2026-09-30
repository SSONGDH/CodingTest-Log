# 이름에 el이 들어가는 동물 찾기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59047
- 분류: String, Date
- 푼 날짜:
- 결과: 성공

## 핵심

- `LIKE '%EL%'`: 앞뒤에 뭐가 와도 EL이 포함되면 통과
- 개만: `ANIMAL_TYPE = 'Dog'`

## 막혔던 부분

## 배운 점

| 패턴 | 의미 |
|---|---|
| `'%EL%'` | EL 포함 |
| `'EL%'` | EL로 시작 |
| `'%EL'` | EL로 끝 |
| `'_EL'` | 아무 글자 1개 + EL |

- MySQL의 `LIKE`는 기본적으로 대소문자를 구분하지 않아 `Elijah`, `Mitty`의 `el` 모두 잡힘
- 문자열은 큰따옴표보다 **작은따옴표**가 표준 (MySQL은 둘 다 되지만 다른 DB는 큰따옴표를 컬럼명으로 인식)
