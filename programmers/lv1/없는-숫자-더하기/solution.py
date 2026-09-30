def solution(numbers):
    answer = 0
    for i in range(1,10):
        if(numbers.count(i)>0):
            continue
        else:
            answer+=i
    
    return answer
