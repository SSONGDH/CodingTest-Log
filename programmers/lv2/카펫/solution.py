def solution(brown, yellow):
    answer=[0,0]
    for i in range(1, (yellow+1)//2+2):
        if(yellow%i==0):
            if(((yellow//i)*2+2*i+4)==brown ):
                answer[0]=(i+2)
                answer[1]=(yellow//i+2)


    return answer
