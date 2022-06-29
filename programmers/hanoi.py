answer = []

def move(n, now, target):
    temp = [1,2,3]
    temp.remove(now)
    temp.remove(target)
    temp = temp[0]
    if n == 1:
        answer.append([now,target])
    else:
        move(n-1, now, temp)
        answer.append([now,target])
        move(n-1, temp, target)  

def solution(n):
    move(n, 1, 3)
    return answer