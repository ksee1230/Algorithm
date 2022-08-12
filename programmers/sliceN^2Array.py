# 프로그래머스 - n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    return [max(i//n+1, i%n+1) for i in range(left, right+1)]