def solution(arr):
    answer = []
    if(len(arr)==1):
        answer=arr
    for i in range(len(arr)-1):
    
        if(i==len(arr)-2):
            if(arr[i]==arr[i+1]):
                answer.append(arr[i])
            else:
                answer.append(arr[i])
                answer.append(arr[i+1])
        elif(arr[i]==arr[i+1]):
            continue
        else:
            answer.append(arr[i])


    return answer
