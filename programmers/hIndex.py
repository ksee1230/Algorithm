# 처음에는 H-index가 인용된 횟수 중 하나여야 한다고 생각하고 code를 작성
# 그런데 그게 아니라 papers-citations 로 plot 한 다음 citations = papers 그래프를 그리고
# 이 그래프의 위에 있는 점의 개수를 구하는 게 정답이었다
# 그래서 내림차순으로 정렬하고 위 조건에 맞는 개수를 구했음
# for문을 끝까지 돌았다는 의미는 모든 논문이 n회 이상 인용되었다는 의미이기에
# for-else 문을 통해 n을 return 하도록 하였다

def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i, v in enumerate(citations):
        if(i+1 > v):
            return i
    else:
        return n