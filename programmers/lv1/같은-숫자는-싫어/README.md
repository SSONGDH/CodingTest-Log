# 같은 숫자는 싫어

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12906
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- `arr[i]`와 `arr[i+1]`을 비교해서 다를 때만 추가
- 마지막 두 원소와 길이 1인 경우를 따로 처리

## 막혔던 부분

- "다음 값"과 비교하다 보니 마지막 원소 처리가 복잡해짐

## 다른 풀이에서 배운 점

- 다음 값 대신 **`answer`에 마지막으로 넣은 값(`answer[-1]`)** 과 비교하면 예외 처리가 필요 없음 (스택 사고방식)

```python
def solution(arr):
    answer = []
    for x in arr:
        if not answer or answer[-1] != x:
            answer.append(x)
    return answer
```
