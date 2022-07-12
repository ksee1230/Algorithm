# 구성 가능한 모든 숫자를 다 만들고
# 가장 큰 수를 찾고
# 에라토스테네스의 체로 숫자들 중 소수가 몇 개인지 판별
from itertools import permutations

def prime(n):
    arr = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if arr[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = False
    return primes

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    perm = []
    
    for i in range(1, len(numbers)+1):
        perm += list(permutations(numbers, i))
        
    numbers = list(set([int(("").join(p)) for p in perm]))
    bigN = max(numbers)
    primes = prime(bigN)
    for number in numbers:
        if number in primes:
            answer += 1
    return answer