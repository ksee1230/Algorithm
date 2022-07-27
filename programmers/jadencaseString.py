def solution(s):
    answer = ''
    token = 1
    for ss in s:
        if token == 1:
            answer += ss.upper()
            token = 0
        else:
            answer += ss.lower()
        
        if ss == ' ':
            token = 1
        
    return answer