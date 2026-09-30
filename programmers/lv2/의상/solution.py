def solution(clothes):
    closet = {}
    for name, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1

    answer = 1
    for count in closet.values():
        answer *= (count + 1)

    return answer - 1
