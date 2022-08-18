# 프로그래머스 - 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    record = list(map(lambda x : x.split(' '), record))
    idNick = {}
    for r in record:
        if r[0] != 'Leave':
            idNick[r[1]] = r[2]
    
    for r in record:
        if r[0] == 'Enter':
            answer.append(idNick[r[1]]+"님이 들어왔습니다.")
        elif r[0] == 'Leave':
            answer.append(idNick[r[1]]+"님이 나갔습니다.")
    return answer