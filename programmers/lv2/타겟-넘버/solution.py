def solution(numbers, target):
    result = [0]

    while numbers:
        temp = numbers.pop()
        new_result = []

        for i in range(len(result)):
            new_result.append(result[i] + temp)
            new_result.append(result[i] - temp)

        result = new_result

    return result.count(target)
