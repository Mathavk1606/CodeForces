import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().strip().split()))
rgrid = lambda n: [list(map(int, input().split())) for _ in range(n)]

def solve():
    a,b,n = rlist()
    arr = rlist()
    
    max_time_for_bomb = b
    for i in arr:
        max_time_for_bomb += min(a-1,i)
    print(max_time_for_bomb)
            
    
        

for tc in range(rint()):
    solve()