import sys
from collections import Counter
import math 

input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    n = rint()
    while n % 2 == 0:
        n //= 2
	
    if n > 1:
	    return ["YES"]  
    else:
	    return ["NO"]
        
for _ in range(rint()):
    res = solve()
    print(*res)