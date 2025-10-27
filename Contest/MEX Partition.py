import sys
from collections import Counter
input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    arr = rlist()
    count = Counter(arr)
    res = []
    mex = 0
    while mex in count:
        mex += 1
    
    res.append(mex)
    return res

for _ in range(rint()):
    res = solve()
    print(*res)