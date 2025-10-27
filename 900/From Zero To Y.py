import sys
from collections import Counter
import math 

input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    x,y = rlist()
    
    possible = [1,x]
    
    n = 10
    while n < y:
        possible.append(x*n)
        n *= 10
    
    operations = 0
    
    for i in range(len(possible)-1,-1,-1):
        if y%possible[i] == 0:
            operations += y//possible[i]
            break
        else:
            possible_removals = y//possible[i]
            operations += possible_removals
            y -= possible_removals*possible[i]
    
    return [operations]
    
    
    #k = k +1
    #k = k + x*(10**p) p>=0
    
    

for _ in range(rint()):
    res = solve()
    print(*res)