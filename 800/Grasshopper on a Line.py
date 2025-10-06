t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    x,k = arr[0], arr[1]
    ans = []
    for i in range(x,0,-1):
        if i%k!=0:
            q = x//i
            x = x%i
            for _ in range(q): ans.append(i)
    print(len(ans))
    strans = " ".join(map(str,ans))
    print(strans)
            
            
    
