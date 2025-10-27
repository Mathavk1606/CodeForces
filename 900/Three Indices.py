import sys
from collections import Counter
import math 

input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    arr = rlist()
    ans = []
    for j in range(1, n - 1):
        if arr[j - 1] < arr[j] and arr[j] > arr[j + 1]:
            ans = [j, j + 1, j + 2]
            break
    return ans

for _ in range(rint()):
    res = solve()
    if len(res) == 3:
        print("YES")
        print(*res)
    else:
        print("NO")