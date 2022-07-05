def solution(n):
    arr = [0 for _ in range(n+1)]
    arr[0], arr[2] = 1, 3
    temp = 1
    for i in range(4, n+1, 2):
        arr[i] = arr[i-2] * 3 + temp * 2
        temp += arr[i-2]
    
    return arr[n] % 1000000007

# dp문제
# dp를 풀 때는 너무 어려운 길로 가지 않도록 유의하자
# 언제나 답은 생각보다 간단하다