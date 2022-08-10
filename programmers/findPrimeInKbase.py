def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    else:
        return True

def solution(n, k):
    arr = ""
    answer = 0
    while n>0:
        n, m = divmod(n,k)
        arr += str(m)
    arr = list(map(int, list(filter(lambda x: len(x) > 0, arr[::-1].split('0')))))
    
    for a in arr:
        if isPrime(a):
            answer += 1
    return answer