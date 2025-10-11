import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().strip().split()))
rgrid = lambda n: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n,k,x = rlist()
    min_sum = k * (k + 1) // 2
    max_sum = n * (n + 1) // 2 - (n - k) * (n - k + 1) // 2
    print("YES" if min_sum <= x <= max_sum else "NO")
            
    
        

for tc in range(rint()):
    solve()