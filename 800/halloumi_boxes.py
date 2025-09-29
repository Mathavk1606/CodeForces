t = int(input())
for  _ in range(t):
    n,k = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    x = sorted(arr)
    if arr == x or k > 1: print("Yes")
    else: print("No")