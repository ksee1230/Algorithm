# 어쩌다 보니 3xn 타일링을 먼저 풀었었다..
# 그냥 피보나치

def solution(n):
    arr = [0]*(n+1)
    arr[0], arr[1] = 1, 1
    for i in range(2, n+1):
        arr[i] = (arr[i-1]%1000000007 + arr[i-2]%1000000007)%1000000007
    return arr[n]