import sys
from collections import Counter
input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    arr = rlist()
    total_and = arr[0]
    for i in range(1,n):
        total_and &= arr[i]
    return [total_and]
        
for _ in range(rint()):
    res = solve()
    print(*res)