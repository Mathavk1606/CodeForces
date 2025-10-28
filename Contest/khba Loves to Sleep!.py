for _ in range(int(input())):
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    arr_set = set(arr)  
    res = []
    
    for i in range(x, -1, -1):
        if i not in arr_set:
            res.append(i)
            if len(res) == k: 
                break
    
    result = res if len(res) >= k else arr
    print(" ".join(map(str, result)))