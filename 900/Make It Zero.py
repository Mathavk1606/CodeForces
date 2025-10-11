import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
rint = lambda: int(input())
rlist = lambda: list(map(int, input().strip().split()))
rgrid = lambda n: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n = rint()
    arr = rlist()
    if n % 2 == 0: 
        print("2")          
        print(f"1 {n}")     
        print(f"1 {n}")    
    else:  
        print("4")
        print(f"1 {n - 1}")
        print(f"1 {n - 1}")
        print(f"{n - 1} {n}")
        print(f"{n - 1} {n}")
    
        

for tc in range(rint()):
    solve()