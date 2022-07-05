import math

def solution(progresses, speeds):
    answer = []
    days = []
    result, currentDay = 0, 0
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        
        if currentDay == 0:
            currentDay = day
            result += 1
        elif day <= currentDay:
            result += 1
        else:
            answer.append(result)
            currentDay = day
            result = 1
            
    answer.append(result)
    return answer

# python의 경우 두 배열에서 같은 index에 있는 값들을 뽑아올 때 zip으로 배열을 묶고 a,b 와 같은 tuple 형태로 뽑는 것이 효율적이다.
# push summary를 잘못 적어서 다시 push