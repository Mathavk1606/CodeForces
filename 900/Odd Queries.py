import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n,q = rlist()
    arr = rlist()
    oldSum = sum(arr)
    res = []
    
    prefix = [0] * (n+1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    #2 2 1 3 2
    #0 2 4 5 8 10
            
    for _ in range(q):
        l,r,k = rlist()
        sum_to_remove = prefix[r] - prefix[l - 1]
        sum_to_add = (r - l + 1) * k
        total_sum = oldSum - sum_to_remove + sum_to_add

        if total_sum % 2 == 1:
            res.append("YES")
        else:
            res.append("NO")
        
    return res

for _ in range(rint()):
    res = solve()
    print(*res)

