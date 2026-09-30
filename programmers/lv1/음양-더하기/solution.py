def solution(absolutes, signs):
    total=0
    for i in range(len(absolutes)):
        if(signs[i]==False):
            total+=absolutes[i]*(-1)
        else:
            total+=absolutes[i]
    return total
