# 조건에 맞는 도서와 저자 리스트 출력하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144854
- 분류: JOIN
- 푼 날짜:
- 결과: 성공

## 핵심

- 도서(`BOOK`)와 저자(`AUTHOR`)를 `AUTHOR_ID`로 조인해서 저자 이름을 가져옴
- 경제 카테고리만, 출판일 오름차순

## 막혔던 부분

## 배운 점

- 모든 책에 저자가 있어서 `LEFT JOIN`도 결과가 같았지만, "양쪽에 다 있는 것"이 목적이면 `INNER JOIN`(`JOIN`)이 의도에 맞음
- `%`가 없는 `LIKE`는 사실상 `=`와 같으니 `CATEGORY = '경제'`가 더 명확함
