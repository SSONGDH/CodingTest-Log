# 기능개발

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: 성공

## 접근 방법

- 하루씩 시뮬레이션: 모든 작업에 속도를 더함
- 맨 앞 작업이 100 이상이면 `popleft()`로 빼면서 개수를 셈 (뒤 작업은 앞 작업이 끝나야 배포 가능)
- 그날 배포된 개수가 있으면 `answer`에 추가

## 막혔던 부분

## 다른 풀이에서 배운 점

- 두 번째 반복은 "맨 앞이 100 이상인 동안"이라는 뜻이라 `while`이 더 자연스러움

```python
while progresses and progresses[0] >= 100:
    count += 1
    progresses.popleft()
    speeds.popleft()
```

- 하루씩 돌리지 않고 **작업별 남은 일수**를 먼저 계산하는 방법도 있음

```python
def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        days.append((100 - p + s - 1) // s)   # 올림 나눗셈

    answer = []
    front = days[0]
    count = 0
    for d in days:
        if d <= front:
            count += 1
        else:
            answer.append(count)
            front = d
            count = 1
    answer.append(count)
    return answer
```
