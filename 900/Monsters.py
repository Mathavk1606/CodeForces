for _ in range(int(input())):
    n,k = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    modArr = [(arr[i]%k if arr[i]%k != 0 else k, i+1) for i in range(n)]
    modArr.sort(key=lambda x: (-x[0], x[1]))
    print(' '.join(str(item[1]) for item in modArr))