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