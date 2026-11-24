n,T=(map(int,input().split()))
nums=list((map(int,input().split())))
answer=[]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if(i!=j and i!=k and j!=k):
                if(T>=nums[i]+nums[j]+nums[k]):
                    if len(answer)==0:
                        answer.append(nums[i]+nums[j]+nums[k])
                    
                    else:
                        if(T-answer[0]>=T-(nums[i]+nums[j]+nums[k])):
                            answer[0]=nums[i]+nums[j]+nums[k]

                    



print(answer[0])
            
            
    
