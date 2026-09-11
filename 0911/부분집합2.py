lst = [1, 2, 3, 4, 5]
N = 5

# 합이 S이하인 부분집합을 구하세요.
S = 6

# 부분집합(재귀함수)
# idx : 재귀함수 단계 -> 내가 부분집합에 포함할지 안할지 고민하고 있는 인덱스 번호
# 나는 현재 idx번 원소를 부분집합에 넣을지 말지 고민중 ...
# selected : 내가 고른 원소의 상태를 나타낸다.
# selected[x] ==1 : x번 원소를 부분집합에 포함시켰다.
# selected[y] ==0: y번 원소를 부분집합에 포함시키지 않았다.
# 내가 고른 원소의 상태는 다음 단계에서도 이어지기 때문에 파라미터로 전달
# s : 지금까지 만든 부분집합의 합
def make_set(idx,selected,s):

    # 0. 가지치기
    # 현재까지 내가 구한 부분집합의 합이 s 인데
    # 문제는 합이 S이하인 부분집합을 구하는 것이다
    # 이미 더 커져서 뒤에 있는 어느 원소를 고르더라도 S보다 커질 것이다.
    # 이 뒤는 더 이상 진행할 필요가 없다.(답이 될 가능성 X)
    if s > S:
        return

    # 1. 종료 조건
    if idx == N:
        # 지금까지의 결과를 종합
        subset=[]
        for i in range(N):
            if selected[i]:
                subset.append(lst[i])

        print(subset)
        return

    # 2. 재귀 호출 (다음단계)
    # idx번 원소를 부분집합에 포함시키기로 했다 -> 다음단계(idx+1)
    selected[idx] =1
    make_set(idx+1,selected,s+lst[idx])

    # idx번 우너소를 부분집합에 포함시키지 않기로 했다 -> 다음단계(idx+1)
    selected[idx]=0
    make_set(idx+1,selected,s)

# 0번 원소부터 부분집합 포함여부 고려, 아직 아무것도 고르지 않은 상태 [0]*5
make_set(0, [0] * N,0)