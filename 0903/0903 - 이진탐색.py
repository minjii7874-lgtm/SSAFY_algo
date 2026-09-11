T = int(input())

for i in range(1, T+1):
    P, A, B = map(int, input().split())

def binary_search(a, N, key):
    start=0
    end=N-1
    while start<=end:
        middle = (start + end) // 2
        if a[middle] ==key:
            return middle
        elif a[middle] > key:
            end = middle -1

        else:
            start = middle +1

    return -1

