# 길이로 정렬하고 자신보다 길이가 긴 요소에 대해 자신 길이 만큼을 잘라서 비교
# 같은게 있으면 return false, 끝까지 다 돌았을 때는 return true
# 정확성은 됐는데 효율성에서 문제 발생
# zip으로 효율성이 올라갔다는 글을 보고 비교를 나보다 긴 모두와 할 필요 없다는 걸 깨달음
# 수정
# 길이로 sort를 하지말고 그냥 sort를 하면 String이기 때문에 사전식으로 정렬이 되는데
# 접두 관계인 번호들이 있으면 무조건 바로 다음으로 정렬될 수 밖에 없기 때문에
# 실제로는 비교를 바로 다음 번호와만 수행하면 된다
# zip과 startswith() 을 이용해서 좀 더 간단하게 풀이 가능
# 해시에 문제가 카테고라이즈 되어 있으니 해시를 사용하는게 맞는 것 같은데
# 도통 어떻게 하는 지 감을 못 잡아서 검색해보니 해시 테이블의 삽입, 삭제, 검색에 O(1)이 걸리기에
# 이를 이용하여 그냥 빠르게 검색을 하는 구조였다
# python은 dict가 있어서 그냥 이걸 사용하면 되는데, 다른 언어에서는 해시를 어떤 식으로 구현해야 하는지 숙지해야 할 듯

# 실제로 효율성 검사를 하니 해시가 가장 느리고(solution), 그 다음이 solution1, zip을 사용한 solution2가 가장 빨랐다.
# 해시가 빠르다고는 하지만, 다 검사하는 것이 수행이 오래 걸리는 것으로 보인다
# 이건 근데 그냥 python이라 그런 거 아닐까?

def solution(phone_book):
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = 1
    for phone in phone_book:
        tmp = "";
        for num in phone:
            tmp += num
            if tmp in phone_dict and tmp != phone:
                return False
    else: return True

def solution1(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        phone = phone_book[idx]
        if(phone_book[idx+1][:len(phone)] == phone):
            return False
    else:
        return True


def solution2(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True