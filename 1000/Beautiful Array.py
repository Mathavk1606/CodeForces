import math
for _ in range(int(input())):
    n, k, b, s = map(int, input().split())
    ans = [0] * n 
    minSum = k*b
    maxSum = k*b + (k-1)*n
    
    if s < minSum or s > maxSum:
        print(-1)
    else:
        ans[0] = minSum
        s -= minSum
        
        for i in range(n):
            add = min(k-1, s)
            ans[i] += add
            s -= add
        
        print(' '.join(map(str, ans)))