t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_xor = 0 
    for num in arr:
	    total_xor ^= num 

    if n % 2 == 1: 
        print(total_xor)  
    else:  
	    if total_xor == 0:  
		    print(total_xor)
	    else:
	        print(-1)
        
    
