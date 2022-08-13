# 프로그래머스 - 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report = list(set(report))
    reportedId = {}
    for r in report:
        reporter, reported = r.split(' ')
        if reported not in reportedId:
            reportedId[reported] = [reporter]
        else:
            reportedId[reported].append(reporter)
            
    for value in reportedId.values():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1
                
    return answer