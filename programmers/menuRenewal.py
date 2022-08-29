# 프로그래머스 - 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    maxCount = {c: 2 for c in course}
    dic = {}
    for order in orders:
        for c in course:
            if len(order) >= c:
                temp = list(combinations(order, c))
                for t in temp:
                    t = ''.join(sorted(list(t)))
                    if t not in dic:
                        dic[t] = 1
                    else:
                        dic[t] += 1
                        maxCount[c] = max(maxCount[c], dic[t])
    for key, value in dic.items():
        if maxCount[len(key)] == value:
            answer.append(key)
    
    answer.sort()
        
    return answer