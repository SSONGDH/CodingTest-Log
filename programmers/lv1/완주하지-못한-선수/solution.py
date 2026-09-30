def solution(participant, completion):
    A = sorted(participant)
    B = sorted(completion)

    for i, value in enumerate(A):
        if i >= len(B) or value != B[i]:
            return value
