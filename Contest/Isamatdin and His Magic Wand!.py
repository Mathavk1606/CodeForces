for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    oddcnt = 0
    evencnt = 0
    
    for i in arr:
        if i % 2 == 0:
            evencnt += 1
        else:
            oddcnt += 1
    
    if oddcnt == n or evencnt == n:
        print(" ".join(map(str, arr)))
    else:
        arr.sort()
        print(" ".join(map(str, arr)))