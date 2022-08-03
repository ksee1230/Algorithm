def solution(s):
    answer = [0,0]
    
    while (s!="1"):
        answer[1], length = answer[1] + s.count("0"), s.count("1")
        s = format(length, 'b')
        answer[0] += 1
    return answer