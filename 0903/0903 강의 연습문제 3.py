arr = [-7, -5, 2, 8, -2, 4, 6, 9, 12]

n = len(arr)

for i in range(1<<n):
    total =0
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=",")
            total +=arr[j]
    print()

    if total ==0:
        print("합이 0인 부분집합 존재")
