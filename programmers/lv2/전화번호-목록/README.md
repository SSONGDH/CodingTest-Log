# 전화번호 목록

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: AI 풀이 참고 → 다시 풀기 필요

## 접근 방법

- 문자열로 정렬하면 접두어 관계인 번호끼리 **바로 옆에** 붙음 (`"119"`, `"1195524421"`)
- 그래서 인접한 두 번호만 `startswith`로 비교하면 됨

## 막혔던 부분

- AI 풀이를 참고함
- 이중 for문으로 모든 쌍을 비교하면 번호가 최대 100만 개라 시간 초과

## 다른 풀이에서 배운 점

- 이 문제의 원래 분류는 **해시**. 모든 번호를 `set`에 넣고, 각 번호의 앞부분이 `set`에 있는지 확인

```python
def solution(phone_book):
    numbers = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in numbers:
                return False
    return True
```

- `set`에서 `in`은 O(1), 리스트에서 `in`은 O(N)
