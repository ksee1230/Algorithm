# 2xn 타일링..?

def solution(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = (a + b)%1234567, a
    return a
