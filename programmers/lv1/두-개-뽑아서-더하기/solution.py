def solution(numbers):
    answer = []
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if i == j:
                continue

            if answer.count(a + b) == 0:
                answer.append(a + b)
    answer.sort()
    return answer
