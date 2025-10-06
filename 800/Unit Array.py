t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    negative_count = arr.count(-1)
    positive_count = arr.count(1)
    
    ans = 0
    while positive_count < negative_count or negative_count % 2 == 1:
        ans += 1
        positive_count += 1 
        negative_count -= 1
    print(ans)
    
            
            
    
