num=list((map(int,input().split())))
num.sort()

while True:
    if(num[0]+num[1]>num[2] and num[1]+num[2]>num[0] and num[0]+num[2]>num[1]):
        print(num[0]+num[1]+num[2])
        break

    num[2]-=1
    num.sort()
    
