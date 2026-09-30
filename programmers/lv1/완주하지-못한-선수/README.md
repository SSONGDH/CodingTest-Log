# 완주하지 못한 선수

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
- 난이도: Lv.1
- 푼 날짜:
- 소요 시간:
- 결과: 성공 (정렬 풀이)

## 접근 방법

- 두 명단을 정렬하면 같은 위치끼리 이름이 같아야 함
- 처음으로 이름이 다른 위치, 또는 `completion`이 끝난 뒤의 마지막 참가자가 정답

## 막혔던 부분

## 다른 풀이에서 배운 점

- 정렬은 O(N log N), 딕셔너리로 이름 개수를 세면 O(N)
- **Lv2 해시 문제(전화번호 목록, 의상)의 뼈대**라서 딕셔너리 풀이로 다시 쳐보기

```python
def solution(participant, completion):
    count = {}
    for name in participant:
        count[name] = count.get(name, 0) + 1
    for name in completion:
        count[name] -= 1
    for name in count:
        if count[name] > 0:
            return name
```
