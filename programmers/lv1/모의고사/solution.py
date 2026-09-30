def solution(answers):
    answer=[]
    countA=0
    countB=0
    countC=0
    
    checkA=1
    checkB=1
    checkC=[3,3,1,1,2,2,4,4,5,5]
    for i in answers:
        if(checkA==i):
            countA+=1
            
        checkA+=1
        if(checkA==6):
            checkA=1
    
    for j, value in enumerate(answers):
        if(j%2==0):
            if(value==2):
                countB+=1
        else:
            if(value==checkB):
                countB+=1
                
            if(checkB==1):
                checkB+=2
            else:
                checkB+=1
                
            if(checkB==6):
                checkB=1
                
    for k, value in enumerate(answers):
        if(value==checkC[k%len(checkC)]):
            countC+=1
    
    temp=[countA,countB,countC]
    


    
    for q, values in enumerate(temp):
        if(values == (max(temp))):
            answer.append(q+1)
    
    answer.sort()
    return answer
