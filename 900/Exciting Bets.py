import sys
from collections import Counter
import math 

input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    a,b = rlist()
    if a == b:
        return [0,0]
    
    max_exitement = abs(a-b)
    
    # op1 = 0
    # x1,y1 = a,b
    # while math.gcd(x1,y1) != max_exitement:
    #     x1 += 1 
    #     y1 += 1
    #     op1 +=1
    
    # op2 = 0
    # x2,y2 = a,b
    # while math.gcd(x2,y2) != max_exitement:
    #     x2 += -1 
    #     y2 += -1
    #     op2 += 1 
    
    
    return [max_exitement,min(b%max_exitement,max_exitement - b%max_exitement)]
    
        
for _ in range(rint()):
    res = solve()
    print(*res)