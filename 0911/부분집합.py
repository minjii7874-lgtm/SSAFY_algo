lst = [1, 2, 3, 4, 5]
N = 5


# 부분집합(재귀함수)
# idx : 재귀함수 단계 -> 내가 부분집합에 포함할지 안할지 고민하고 있는 인덱스 번호
# 나는 현재 idx번 원소를 부분집합에 넣을지 말지 고민중 ...
# selected : 내가 고른 원소의 상태를 나타낸다.
# selected[x] ==1 : x번 원소를 부분집합에 포함시켰다.
# selected[y] ==0: y번 원소를 부분집합에 포함시키지 않았다.
# 내가 고른 원소의 상태는 다음 단계에서도 이어지기 때문에 파라미터로 전달
def make_set(idx,selected):
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
    make_set(idx+1,selected)

    # idx번 우너소를 부분집합에 포함시키지 않기로 했다 -> 다음단계(idx+1)
    selected[idx]=0
    make_set(idx+1,selected)

# 0번 원소부터 부분집합 포함여부 고려, 아직 아무것도 고르지 않은 상태 [0]*5
make_set(0, [0] * N)