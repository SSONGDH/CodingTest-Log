from collections import deque
def solution(progresses, speeds):

    answer = []
    progresses = deque(progresses)
    speeds=deque(speeds)
    while(progresses):
        count=0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
            
        for j in range(len(progresses)):
            if(progresses[0]>=100):
                count+=1
                progresses.popleft()
                speeds.popleft()
        
        if(count>0):
            answer.append(count)
    return answer
