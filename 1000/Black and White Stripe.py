for _ in range(int(input())):
    n,k = map(int,input().split(" "))
    s = input()
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if s[i] == 'W' else 0)
	
    ans = float('inf')
	
    for i in range(n - k + 1):
        diff = prefix[i + k] - prefix[i]
        ans = min(ans, diff)
	
    print(ans)