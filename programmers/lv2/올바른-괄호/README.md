# 올바른 괄호

- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909
- 난이도: Lv.2
- 푼 날짜:
- 소요 시간:
- 결과: 성공 (스택 개념 검색 후 직접 구현)

## 접근 방법

- `(`면 스택에 넣고, `)`면 스택에서 하나 뺌
- `)`인데 스택이 비어 있으면 짝이 없으니 `False`
- 끝났는데 스택에 남아 있으면 닫히지 않은 괄호가 있으니 `False`

## 막혔던 부분

- 스택 개념을 검색해서 확인함

## 다른 풀이에서 배운 점

- 마지막 판단은 `return len(stack) == 0` 한 줄로 가능
- 괄호가 한 종류라서 스택 대신 **개수 카운터**로도 풀림

```python
def solution(s):
    count = 0
    for c in s:
        count += 1 if c == '(' else -1
        if count < 0:
            return False
    return count == 0
```
