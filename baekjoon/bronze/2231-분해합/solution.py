n=int(input())

flag=0
for i in range(1,n+1):
    list=[]

    temp=i
    while temp>0:
        list.append(temp%10)
        temp//=10

    if(n==i+sum(list)):
        flag=1
        print(i)
        #print(list)
        break

if(flag==0):
    print(0)
