# 3009. 네 번째 점

- 링크: https://www.acmicpc.net/problem/3009
- 난이도: Bronze III
- 분류: 구현, 기하학
- 푼 날짜: 2026-11-24
- 소요 시간:
- 결과: 성공

## 접근 방법

- 축에 평행한 직사각형은 x좌표 2종류, y좌표 2종류가 **각각 2번씩** 나옴
- 세 점에서는 하나만 1번 나오고, 그게 네 번째 점의 좌표
- x좌표끼리(`first`), y좌표끼리(`second`) 모아서 `count(i) == 1`인 값 찾기

## 막혔던 부분

- 없음

## 다른 풀이에서 배운 점

### 출력 형식

- 지금 코드는 x와 y를 **두 줄로** 출력함. 문제의 예제 출력은 `7 7`처럼 **한 줄**
- 정답 처리가 됐더라도 예제 형식에 맞춰 한 줄로 출력하는 습관 들이기

```python
first, second = [], []
for _ in range(3):
    a, b = map(int, input().split())
    first.append(a)
    second.append(b)

x = [i for i in first if first.count(i) == 1][0]
y = [i for i in second if second.count(i) == 1][0]
print(x, y)          # print에 여러 개 넣으면 공백으로 구분해서 한 줄
```

### XOR 풀이

- 같은 수를 두 번 XOR하면 0이 되므로 세 개를 XOR하면 한 번 나온 값만 남음

```python
x = y = 0
for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b
print(x, y)
```

- "두 번 나온 것들 사이에서 한 번 나온 것 찾기"에 쓰는 트릭
