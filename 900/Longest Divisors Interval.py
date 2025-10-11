import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().strip().split()))
rgrid = lambda n: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n = rint()
    i = 1
    while n % i == 0: 
        i += 1  
    print(i-1)

for tc in range(rint()):
    solve()