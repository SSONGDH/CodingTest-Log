def solution(array, commands):
    answer = []
    
    for j in commands:
        temp=[]
        for i in range(j[0]-1,j[1]):
            print("i:",i)
           # print(array[i])
            temp.append(array[i])

        temp.sort()
        print("cc")
        print(temp)
    #    print("d: ",temp[j[2]-1])
        answer.append(temp[j[2]-1])
    
    
    return answer
