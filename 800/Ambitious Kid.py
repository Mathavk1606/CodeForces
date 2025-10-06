n = int(input())
arr = list(map(int,input().split(" ")))
if arr.count(0) > 0: print(0)
else:
    val = float('inf')
    for i in arr:
        val = min(val,abs(i))
    print(val)
    