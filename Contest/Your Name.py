from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s,t = map(str,input().split(" "))
    
    sMap = defaultdict(int)
    tMap = defaultdict(int)
    
    for i in s:
        sMap[i] += 1
    
    for j in t:
        tMap[j] += 1
    
    if sMap == tMap:
        print("Yes")
    else:
        print("No")
    
    