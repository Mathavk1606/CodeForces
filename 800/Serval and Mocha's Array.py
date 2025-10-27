import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    is_beautiful = False
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(a[i],a[j]) <= 2:
                is_beautiful = True
    if is_beautiful:
        print("Yes")
    else:
        print("No")
            