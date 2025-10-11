import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().strip().split()))
rgrid = lambda n: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n,k = rlist()
    s = input()
    frqC = Counter(s)
    
    odd_counts = 0
    for char_count in frqC.values():
        if char_count % 2 != 0:
            odd_counts += 1
    
    if k >= odd_counts - 1:
            print("YES")
    else:
        print("NO")
        

for tc in range(rint()):
    solve()