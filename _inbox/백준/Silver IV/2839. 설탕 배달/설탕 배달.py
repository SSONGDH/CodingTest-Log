a=int(input())

x=a//5
y=a//3
answer=-1


for i in range(0,x+1):
    for j in range(0,y+1):
        if(i*5+j*3==a):
            if(answer==-1):
                answer=i+j
            answer=min(answer,i+j)

print(answer)
        
