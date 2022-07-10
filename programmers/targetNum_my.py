# 타겟 넘버의 떠오르는 풀이를 구현
# 각 숫자마다 부호가 +, -로 결정되기 때문에 확인해야 하는 총 가지수는 2^n개
# 그래서 0 ~ (2^n - 1)의 범위로 반복문을 실행하면서 수를 이진수로 변환하여
# 이진수가 0이면 해당 위치의 수를 -로, 1이면 해당 위치의 수를 +로 하여
# 해당 계산의 결과가 target과 같으면 정답 수를 1씩 올림

# 모든 가지수를 순차적으로 다 보기 때문에 dfs와 계산속도가 비슷하나, dfs라고 하기엔 어렵다. 

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    for i in range(2**n):
        temp = format(i, 'b').zfill(n)
        total = 0
        for number, t in zip(numbers, temp):
            if t == '0':
                total -= number
            else:
                total += number
        if total == target:
            answer += 1
    return answer