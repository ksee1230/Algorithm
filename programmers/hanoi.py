def move(n, now, target, arr):
    temp = [1,2,3]
    temp.remove(now)
    temp.remove(target)
    temp = temp[0]
    if n == 1:
        arr.append([now,target])
    else:
        move(n-1, now, temp, arr)
        arr.append([now,target])
        move(n-1, temp, target, arr)  

def solution(n):
    answer = []
    move(n, 1, 3, answer)
    return answer