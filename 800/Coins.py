t = int(input())
for _ in range(t):
    #n = int(input())
    arr = list(map(int, input().split()))
    n,k = arr[0],arr[1]
    #2*x + k*y = n 
    if n % 2 == 0 or (n - k) % 2 == 0:
        print("Yes")
    else:
        print("No")
    
