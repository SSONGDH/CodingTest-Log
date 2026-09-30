# 있었는데요 없었습니다

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59043
- 분류: JOIN
- 푼 날짜:
- 결과: 성공

## 핵심

- 보호 시작(`ANIMAL_INS`)과 입양(`ANIMAL_OUTS`)에 **모두 있는** 동물만 필요하므로 `INNER JOIN`
- 입양일보다 보호 시작일이 늦은 잘못된 데이터: `I.DATETIME > O.DATETIME`
- 날짜도 숫자처럼 `>` `<`로 비교 가능

## 막혔던 부분

## 배운 점

- 두 테이블에 같은 컬럼명(`DATETIME`)이 있으면 `I.`, `O.`처럼 별칭을 꼭 붙여야 함
