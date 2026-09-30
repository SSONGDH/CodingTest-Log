# 모의고사

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 1번: 1~5를 반복하도록 `checkA`를 증가시키고 6이 되면 1로 되돌림
- 2번: 짝수 인덱스는 항상 2, 홀수 인덱스는 1 → 3 → 4 → 5 순으로 `checkB`를 변화시킴
- 3번: 패턴 리스트를 만들고 `k % len(checkC)`로 반복
- 세 점수 중 최댓값과 같은 사람을 모두 추가 (동점 처리)

## 막혔던 부분

- 1, 2번 패턴을 변수 증가 규칙으로 직접 구현하느라 코드가 길어짐

## 다른 풀이에서 배운 점

- 3번처럼 **1, 2번도 패턴 리스트 + `%`** 로 통일하면 반복문 하나로 끝남
- `max(scores)`는 반복문 밖에서 한 번만 구하기
- 번호 순서대로 추가하므로 마지막 `sort()`는 필요 없음

```python
def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    scores = [0, 0, 0]
    for i, a in enumerate(answers):
        for p in range(3):
            if a == patterns[p][i % len(patterns[p])]:
                scores[p] += 1

    best = max(scores)
    return [p + 1 for p in range(3) if scores[p] == best]
```
