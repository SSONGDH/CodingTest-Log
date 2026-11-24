a,b=map(int,input().split())
array=[]


for i in range(a):
    string=input()
    array.append(string)

cy=a-8
cx=b-8

def check_W(y,x):
    count=0
    
    for i in range(y,y+8):
        for j in range(x,x+8):
           # print(i,j)
            if(i%2==0):
                if(j%2==0):
                    if(array[i][j]!='W'):
                        count+=1
                else:
                    if(array[i][j]!='B'):
                        count+=1
            else:
                if(j%2==0):
                    if(array[i][j]!='B'):
                        count+=1
                else:
                    if(array[i][j]!='W'):
                        count+=1

    return count

def check_B(y,x):
    count=0
    
    for i in range(y,y+8):
        for j in range(x,x+8):
           # print(i,j)
            if(i%2==0):
                if(j%2==0):
                    if(array[i][j]!='B'):
                        count+=1
                else:
                    if(array[i][j]!='W'):
                        count+=1
            else:
                if(j%2==0):
                    if(array[i][j]!='W'):
                        count+=1
                else:
                    if(array[i][j]!='B'):
                        count+=1


    return count


for i in range(0,cy+1):
    for j in range(0,cx+1):
        #print("start",i,j)
        if(i==0 and j==0):
            answer=min(check_B(i,j),check_W(i,j))
        else:
            answer=min(check_B(i,j),check_W(i,j),answer)


print(answer)

        
