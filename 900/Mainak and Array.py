import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    arr = rlist()
    res = []
    
    ans = arr[n-1]-arr[0]
    
    for i in range(1,n):
        ans = max(ans,arr[i]-arr[0])
    for i in range(n-1):
        ans = max(ans,arr[n-1]-arr[i])
    for i in range(n-1):
        ans = max(ans,arr[i]-arr[i+1])
        
    res.append(ans)
    return res

for _ in range(rint()):
    res = solve()
    print(*res)

