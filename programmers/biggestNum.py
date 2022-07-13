# 순열로 모든 경우의 수를 만들어서 그중 가장 큰 값 반환
# 시간복잡도 부분에서 문제가 발생할 것이 불보듯 뻔하지만
# 그래도 시도는 해보자
from itertools import permutations

def solution1(numbers):
    numbers = list(map(str, filter(None, numbers)))
    numbers = list(permutations(numbers, len(numbers)))
    arr = [int(("").join(n)) for n in numbers]
    return str(max(arr))

# 역시 어림도 없었다
# 정확성만 따지는 문제에서도 시간 초과가 날 정도로 오래 걸림

# 늘려서(3이면 333333...) 비교하는게 가장 옳은 방법인 듯 하다.
# numbers의 원소가 0 이상 1000 이하이기 때문에 총 4자리까지 늘려서 비교
def solution(numbers):
    answer = ""
    exNums = []
    for idx, num in enumerate(numbers):
        tmp = (str(num)*4)[:4]
        exNums.append((idx, tmp))
    exNums.sort(key=lambda exNum: exNum[1])
    exNums.reverse()
    
    for exNum in exNums:
        answer += str(numbers[exNum[0]])
    
    return str(int(answer))