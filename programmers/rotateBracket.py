def solution(s):
    answer = 0
    opener = ["[", "(", "{"]
    closer = ["]", ")", "}"]
    for i in range(len(s)):
        tempS = s[i:] + s[:i]
        stack = []
        for t in tempS:
            if len(stack) == 0:
                stack.append(t)
                continue
                
            if t in opener:
                stack.append(t)
            else:
                if stack[-1] == opener[closer.index(t)]:
                    stack.pop()
                else:
                    stack.append(t)
        if len(stack) == 0:
            answer += 1
    return answer