# 일단 n진법 사용해서 구현 끝..?
# 애초에 저장을 간단하게 할 수 있는 것 같다
def solution1(n):
    answer = ''
    arr = []
    
    while n:
        n, mod = divmod(n, 3)
        arr.append(mod)
    
    arr.reverse()
    
    while 0 in arr:
        idx = arr.index(0)
        arr[idx-1], arr[idx] = arr[idx-1] - 1, 3
        
        if arr[0] == 0:
            arr.pop(0)
    
    for v in arr:
        if v == 3:
            answer += '4'
        else:
            answer += str(v)
        
    return answer

def solution(n):
    answer = ''
    while n:
        if n%3 == 0:
            answer += '4'
            n = n//3 - 1
        else:
            answer += str(n%3)
            n = n//3
    return answer[::-1]
