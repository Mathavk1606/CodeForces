import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n, k = map(int, input().split())
    arr = rlist()
    arr.sort()
    i = 1
    max_len = 1
    for j in range(1, n):
        if arr[j] - arr[j-1] <= k:
            i += 1 
        else:
            i = 1
        max_len = max(max_len,i)
    
    return [n - max_len]

t = rint()
for _ in range(t):
    res = solve()
    print(*res)
