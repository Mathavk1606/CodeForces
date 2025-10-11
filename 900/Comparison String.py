import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    s = input()
    
    max_dec = 0
    current_dec = 0
    for char in s:
        if char == '>':
            current_dec += 1
        else:
            max_dec = max(max_dec, current_dec)
            current_dec = 0
    max_dec = max(max_dec, current_dec)
    
    max_inc = 0
    current_inc = 0
    for char in s:
        if char == '<':
            current_inc += 1
        else:
            max_inc = max(max_inc, current_inc)
            current_inc = 0
    max_inc = max(max_inc, current_inc)
    
    return [max(max_inc, max_dec) + 1]

for _ in range(rint()):
    res = solve()
    print(*res)

