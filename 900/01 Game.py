import sys
from collections import Counter
import math 
input = sys.stdin.readline
rint = lambda: int(input())
rlist = lambda: list(map(int, input().split()))

def solve():
    s = input().strip()  # Remove newline character
    no_of_zeros = 0
    no_of_ones = 0
    
    for i in s:
        if i == '0':
            no_of_zeros += 1
        elif i == '1':  # Use elif to avoid counting other characters
            no_of_ones += 1
    
    combinations = min(no_of_ones, no_of_zeros)
    
    if combinations % 2 != 0:
        return "DA"
    else:
        return "NET"
        
for _ in range(rint()):
    res = solve()
    print(res)  # No need for *res since it's already a string