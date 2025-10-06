t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in arr:
        ans.append(n+1-i)
    strans = " ".join(map(str,ans))
    print(strans)
    
            
            
    
