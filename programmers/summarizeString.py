def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n//2+1):
        tmpStr = s[0:i]
        count = 1
        res = ""
        a, b = divmod(n, i)
        
        for j in range(1, a):
            curStr = s[i*j:i*(j+1)]
            if curStr == tmpStr:
                count += 1
            else:
                if count == 1:
                    res += tmpStr
                else:
                    res += (str(count) + tmpStr)
                    count = 1
                tmpStr = curStr
        else:
            if count == 1:
                res += tmpStr
            else:
                res += (str(count) + tmpStr)
        
        if b != 0:
            b *= -1
            res += s[b:]
        
        answer = min(answer, len(res))
    return answer