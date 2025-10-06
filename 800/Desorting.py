t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    operations = float('inf')
    for i in range(n - 1):
	    if arr[i] <= arr[i + 1]: 
		    diff = arr[i + 1] - arr[i] 
		    required_operations = diff // 2 + 1 
		    operations = min(operations, required_operations) 
	    else:
		    operations = 0 
    print(operations)

        
            
    
    
    