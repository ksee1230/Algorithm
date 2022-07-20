# 같은 종류의 옷이 몇 개인지 각각 구한 뒤
# 수를 전부 곱하고 1을 뺀다.

def solution(clothes):
    answer = 1
    countClothes = dict()
    for name, kind in clothes:
        if kind in countClothes:
            countClothes[kind] += 1
        else:
            countClothes[kind] = 2
    for val in countClothes.values():
        answer *= val
    return answer - 1