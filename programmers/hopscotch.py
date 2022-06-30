# 계속해서 누적으로 제일 큰 걸 더하는 구조로 진행
# 이런 계열을 DP(dynamic programming)라고 한다
# dp는 한 번한 계산을 다시 하지 않고 저장해놓아서 계산 시간을 줄이는 목표를 가짐

def solution(land):
    arr = [land[0]]
    
    for i in range(1, len(land)):
        temp = [0]*4
        for j in range(4):
            a, b, c = [k for k in range(4) if k != j]
            temp[j] = land[i][j] + max(arr[i-1][a], arr[i-1][b], arr[i-1][c])
        arr.append(temp)
    
    return max(arr[len(land)-1])

# [i for i in range(n) if i != x] 를 통해 어떤 범위에서 특정 숫자를 제외한 값을 뽑아낼 수 있다.