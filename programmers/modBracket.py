# 프로그래머스 - 괄호 변환(60058)
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

# 올바른 괄호 문자열을 판단하는 함수
def rightString(p):
    stack = []
    for pp in p:
        if len(stack) == 0:
            stack.append(pp)
            continue
            
        if pp == "(":
            stack.append(pp)
        else:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(pp)
    
    return (len(stack) == 0)

# 문자열을 균형잡힌 괄호 문자열 2개로 분리하는 함수
def splitString(p):
    left = right = 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
            
        if left == right:
            u, v = p[:i+1], p[i+1:]
            break
    return [u, v]


# 문제에서 주어진 과정을 함수로 구현
def makeRightString(p):
    if len(p) == 0: return p # 1. 빈 문자열인 경우, 빈 문자열 반환
    
    u, v = splitString(p) # 2. 문자열을 두 균형잡힌 괄호 문자열로 분리
    
    if rightString(u): # 3. u가 올바른 괄호 문자열이라면
        return u + makeRightString(v) # 3-1. u에 문자열 v에 대해 1단계부터 다시 수행한 결과를 이어 붙인 후 반환
    else: # 4. u가 올바른 괄호 문자열이 아니라면
        # 4-4. u의 첫 번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 새로운 newU를 생성
        u = ''.join(list(map(lambda x : "(" if x == ")" else ")", u[1:-1])))
        return "(" + makeRightString(v) + ")" + u
        
def solution(p):
    if rightString(p): return p
    else: return makeRightString(p)