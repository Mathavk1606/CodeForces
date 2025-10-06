t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    val = max(arr)
    b = []
    c = []
    for i in arr:
        if val != i:
            b.append(i)
        else:
            c.append(i)
    if len(b) == 0:
	    print(-1) 
    else:
	    print(len(b), len(c))
	    print(' '.join(map(str, b)))
	    print(' '.join(map(str, c)))