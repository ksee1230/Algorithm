def solution(n):
    arr = [0,1]
    for i in range(2,n+1):
        # n번째 피보나치 수를 1234567으로 나눈 나머지를 return
        a = (arr[i-2]%1234567 + arr[i-1]%1234567)%1234567
        arr.append(a)
        
    return arr[n]