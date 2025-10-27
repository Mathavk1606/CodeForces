import sys
from collections import Counter
input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    b = rlist()
    ans = []
    ans.append(1)
    lst = [(b[i]-b[i-1]-i) for i in range(1,n)]
    x = 2
    for i in lst:
        if i == 1:
            ans.append(x)
            x += 1 
        elif i == 0:
            ans.append(ans[-1])
    return ans
    
        
for _ in range(rint()):
    res = solve()
    print(*res)