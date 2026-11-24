# 2798. 블랙잭

- 링크: https://www.acmicpc.net/problem/2798
- 난이도: Bronze II
- 분류: 브루트포싱
- 푼 날짜: 2026-11-24
- 소요 시간:
- 결과: 성공

## 접근 방법

- 카드 3장을 고르는 모든 경우를 3중 for문으로 확인 (`solution.py`)
- `i`, `j`, `k`가 서로 다를 때만 세 카드의 합을 계산
- 합이 `T` 이하이면 지금까지 저장한 `answer[0]`과 비교
  - `T - answer[0] >= T - 합` = 합이 더 크거나 같으면 바꾸기
- 마지막에 `answer[0]` 출력

## 막혔던 부분

## 다른 풀이에서 배운 점

- 정석 풀이와 같은 방식 (재풀이 `solution_2.py` 기준)
- "N장 중 K장 고르기" + N이 작음(100) → **`combinations`로 전부 확인하는 완전 탐색**
- 100C3 = 161,700가지라 전부 돌아도 충분

## 재풀이 (2026-11-24)

- `solution_2.py`: `itertools.combinations(nums, 3)`으로 3장 조합을 바로 만듦
- 최댓값은 `max_sum = 0`에서 시작해서 `max()`로 갱신

| | 첫 풀이 | 재풀이 |
|---|---|---|
| 경우 만들기 | 3중 for문 + `i != j` 등 3개 조건 | `combinations(nums, 3)` |
| 확인하는 경우 수 (N=100) | 100³ = 1,000,000 (같은 조합을 순서만 바꿔 6번씩) | 161,700 |
| 최댓값 저장 | 리스트 `answer[0]`, 비었는지 따로 확인 | 변수 `max_sum` + `max()` |
| 시간 | 468 ms | 70 ms |

```python
# X: 순서만 다른 같은 조합을 여러 번 확인
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                ...

# O: 조합은 한 번씩만
for comb in combinations(nums, 3):
    ...
```

- 직접 for문으로 쓸 때도 `range(i + 1, n)`, `range(j + 1, n)`으로 시작하면 중복 없이 조합만 돎
- 카드는 양수라 합이 0보다 작을 수 없음 → `0`으로 시작하면 "처음인지" 확인하는 분기가 필요 없음
