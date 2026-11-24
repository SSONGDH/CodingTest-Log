first = []   # 각 줄의 첫 번째 숫자들만 모을 리스트
second = []  # 각 줄의 두 번째 숫자들만 모을 리스트

for _ in range(3):
    a, b = map(int, input().split())
    first.append(a)
    second.append(b)


for i in first:
    if(first.count(i)==1):
        print(i)


for i in second:
    if(second.count(i)==1):
        print(i)
