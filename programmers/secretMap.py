# 프로그래머스 - [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        s = format(a|b, "0"+str(n)+"b")
        temp = ""
        for i in range(n):
            if s[i]=="0":
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer