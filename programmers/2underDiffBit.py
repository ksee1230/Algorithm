def f(n):
    if n%2 == 0:
        return n+1
    n = '0' + format(n,'b')
    n = list(n)
    n.reverse()
    for i in range(len(n)-1):
        if n[i]=='1' and n[i+1]=='0':
            n[i], n[i+1] = '0', '1'
            break
    n.reverse()
    return int(''.join(n),2)

def solution(numbers):
    answer = list(map(f, numbers))
    return answer