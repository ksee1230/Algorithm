def solution(n):
    answer = []
    arr = [[0]*i for i in range(n+1)]
    num = 1
    x, y = 0, 0
    for i in range(n, 0, -1):
        if (n-i)%3 == 0:
            for _ in range(i):
                x += 1
                arr[x][y] = num
                num += 1
        elif (n-i)%3 == 1:
            for _ in range(i):
                y += 1
                arr[x][y] = num
                num += 1
        else:
            for _ in range(i):
                x -= 1
                y -= 1
                arr[x][y] = num
                num += 1
    for a in arr:
        answer += a
        
    return answer