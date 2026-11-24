target=int(input())

def check(n):
    while n>10:
        if(n%1000==666):
            
            return True

        n//=10

    return False




total=0
temp=1

while True:
    if check(temp):
        total+=1


    if total==target:
        print(temp)
        break

    temp+=1
    
