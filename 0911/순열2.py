lst = [1,2,3,4,5]
N = 5

# idx : idx번 원소의 자리를 교환하겠다.
def make_perm(idx):

    # 1. 종료 조건
    if idx == N:
        print(lst)
        return

    # 2. 재귀호출
    # idx번 자리에 있는 숫자와 교환할 자리 번호 i를 정한다
    # i의 조건 : 현재 자리번호 idx 이상이어야 한다. (i >=idx)
    # lst[idx], lst[i] = lst[i], lst[idx]
    for i in range(idx, N):
        lst[idx] , lst[i] = lst[i], lst[idx]
        # idx+1번 자리 교환하도록, 다음단계로
        make_perm(idx+1)
        # idx번 자리에 i번 말고 다른 번호와도 자리를 바꾸도록
        # 원상복구
        lst[idx] , lst[i] = lst[i], lst[idx]

make_perm(0)
