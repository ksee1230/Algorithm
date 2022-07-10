# 타겟 넘버의 bfs 구현
# 계산 결과를 queue(구현 방식 상 queue가 아니어도 상관은 없는 듯 하다)에 push, pop하면서 순차적으로 진행
# 세 방식 중 속도가 가장 빠른 것을 확인하였다.(아무래도 numbers의 각 elements를 한 번만 조회하면 되다 보니까 그런 듯)

def solution(numbers, target):
    layer = [0]
    for number in numbers:
        queue = []
        for e in layer:
            queue.append(e+number)
            queue.append(e-number)
        layer = queue.copy()
    
    return layer.count(target)