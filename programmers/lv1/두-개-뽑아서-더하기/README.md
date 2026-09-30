# 두 개 뽑아서 더하기

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68644
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 이중 for문(완전탐색)으로 서로 다른 인덱스 두 개를 골라 합을 구하고, 없는 값만 `answer`에 추가 후 정렬

## 막혔던 부분

## 다른 풀이에서 배운 점

- 안쪽 반복을 `range(i+1, n)`으로 시작하면 같은 쌍을 두 번 보지 않음
- 중복 제거는 `set`이 `count`보다 빠름

```python
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return sorted(answer)
```
