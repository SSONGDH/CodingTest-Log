# K번째수

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 명령마다 `i-1`부터 `j-1`까지 원소를 `temp`에 담고 정렬한 뒤 `k-1`번째 값을 꺼냄

## 막혔던 부분

- 인덱스가 1부터 시작하는 문제라 `-1` 보정이 헷갈려서 `print`로 확인함

## 다른 풀이에서 배운 점

- 슬라이싱 `array[i-1:j]`로 반복문 없이 구간을 자를 수 있음 (끝 인덱스는 포함 안 됨)
- 언패킹 `i, j, k = cmd`로 가독성 향상

```python
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
```
