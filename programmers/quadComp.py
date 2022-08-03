# 재귀함수로 짤 예정
# 자기 size가 1x1 이면 자신의 value에 따라 [1, 0] or [0, 1]을 return,
# 1이 아니면 4등분 한 다음에 4등분의 return 값을 다 받아서 배열들의 0번째와 1번째를 각각 다 더한다
# 0이 4이고, 1이 0면 [1,0] 을 return, 반대의 경우 [0,1] 을 return, 둘 다 아니라면 각각 더한 값을 배열에 넣어 return 한다
# 이렇게 다시 원래까지 돌아와서 최종적으로 다 더한 값을 return 한다

def solution1(arr):
    if len(arr) == 1:
        if arr[0][0] == 0:
            return [1,0]
        else:
            return [0,1]
    
    half = len(arr)//2
    quadArr = [[]]*4
    quadArr[0] = [temp[:half] for temp in arr[:half]] # arr의 [0~half][0~half]
    quadArr[1] = [temp[half:] for temp in arr[:half]] # arr의 [half~end][0~half]
    quadArr[2] = [temp[:half] for temp in arr[half:]] # arr의 [0~half][half~end]
    quadArr[3] = [temp[half:] for temp in arr[half:]] # arr의 [half~end][half~end]
    
    answer = [0, 0]
    for quad in quadArr:
        answer[0], answer[1] = (answer[0]+solution(quad)[0]), (answer[1]+solution(quad)[1])
    
    if answer[0] == 4 and answer[1] == 0:
        return [1, 0]
    elif answer[0] == 0 and answer[1] == 4:
        return [0, 1]
    else:
        return answer

# 이렇게 했는데, 문제가 풀어지긴 하나 시간초과가 난다.. 큰 것부터 그냥 계산을 하고 넘어가는 식으로 해야할 듯 하다
# 배열 slicing으로는 한계가 있는 듯 함

def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def quadComp(a, b, l):
        tg = arr[a][b]
        for i in range (a, a+l):
            for j in range (b, b+l):
                if arr[i][j] != tg:
                    l = l//2
                    quadComp(a, b, l)
                    quadComp(a+l, b, l)
                    quadComp(a, b+l, l)
                    quadComp(a+l, b+l, l)
                    return
        answer[tg]+=1
    
    quadComp(0,0,length)
    return answer