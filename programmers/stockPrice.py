# stack 문제
# index가 곧 초 단위이기 때문에 index에 대한 계산을 통해서 시간을 계산한다.
# 해당 index의 값과 탐색 중인 값을 비교하여 탐색 중인 값이 더 크거나 같다면
# index 초의 가격이 떨어지지 않은 것이니까 탐색 중인 값의 index를 stack에 저장하고, 
# 그렇지 않다면 stack에서 pop 한 다음 지금 index에서 stack에서 pop 한 값을 빼서 answer의
# 해당 index에 저장하는 식.
# 떨어지지 않은 가격은 stack에 계속 남아있을 테니 이 값들은 prices의 length에서 1+index를 빼주는 것으로
# answer의 index 위치에 값을 넣어야 한다.

def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i , price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            tmp = stack.pop()
            answer[tmp] = i - tmp
        stack.append(i)
    
    while stack:
        tmp = stack.pop()
        answer[tmp] = len(prices) - 1 - tmp
    return answer