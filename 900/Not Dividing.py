import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    arr = rlist()
    
    for i in range(n):
        if arr[i] == 1:
            arr[i] += 1
    
    for i in range(n - 1):
        if arr[i + 1] % arr[i] == 0:
            arr[i + 1] += 1

    return arr

for _ in range(rint()):
    res = solve()
    print(*res)

