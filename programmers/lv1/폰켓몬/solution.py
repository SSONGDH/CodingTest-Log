def solution(nums):
    t=len(nums)//2

    check=len((list(set(nums))))
              
    answer = t if t < check else check
        
    return answer
