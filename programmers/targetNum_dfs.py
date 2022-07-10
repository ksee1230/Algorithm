# 타겟 넘버의 dfs 구현
# dfs = stack이라는 강박이 약간 있어서 처음에 좀 헤맸는데
# n-queen과 같이 재귀함수 형태로 구현하면 된다는 힌트를 얻고
# n-queen의 code를 개조하는 식으로 구현..
# 결과는 나왔지만 아직 완전 탐색 알고리즘에 대한 공부는 더 필요하다

def dfs(nbs, tg, idx, res):
    cnt = 0
    if idx == len(nbs):
        if tg == res:
            return 1
        else:
            return 0
    
    for i in (-1, 1):
        temp = res + nbs[idx] * i
        cnt += dfs(nbs, tg, idx+1, temp)
    
    return cnt
        
def solution(numbers, target):
    return dfs(numbers, target, 0, 0)