#1. 자리 정하기 방법
# 0번 자리에 올 숫자 정하기
# 1번 자리에 올 숫자 정하기
# ...
# N-1번 자리에 올 숫자 정하기(마지막 자리는 자동으로 정해짐)
lst=[1,2,3,4,5]
N = 5

# result = [?(0번), ?(1번), ?(2번), ?(3번), ?(4번)]
# idx : 순열의 idx번 자리에 올 원소를 선택하는 중이다 ...(단계)
# selected : 순열을 만들 때 이전에 사용했던 원소를 기억(중복 선택 방지)
# selected[x] ==1 : x번 원소는 이전에 이미 사용했다.
# selected[y] ==0 : y번 원소는 아직 사용한 적이 없다.
# result : 만들어진 순열
def make_perm(idx,selected,result):

    # 1. 종료 조건
    # N-1번까지 누구를 놓을지 선택이 끝난 상태, 더 이상 진행 X
    if idx == N:
        print(result)
        return


    # 2. 재귀 호출 (다음 단계)
    # idx번 자리에 어떤 숫자를 놓을 것인지 선택
    # 단, 이전에 선택한 적이 없는 숫자를 골라야함
    for i in range(N):
        # N개의 원소를 확인, 이전에 사용했던 원소는 건너뜀
        # 이전에 사용한 적 없는 원소라면 idx번 자리에 사용하고, 다음 idx+1번 자리로 이동
        if not selected[i]:
            # i번 숫자를 사용한 적 없다면, 순열의 idx번 자리에 놓고 진행
            selected[i] =1
            result.append(lst[i])
            make_perm(idx+1, selected, result)
            # i번 숫자가 아닌 다른 숫자를 순열의 idx번 자리에 놓기 위해서 원상복구
            result.pop()
            selected[i] = 0
 # 0번 자리부터 , 아직 아무것도 고르지 않은 상태, 결과 순열의 초기 상태
make_perm(0,[0]*N, [])


