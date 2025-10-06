t = int(input())
for _ in range(t):
    #n = int(input())
    arr = list(map(int, input().split()))
    if arr[3] < arr[1]:
        print(-1)
    else:
        moves = arr[3]-arr[1]
        arr[0] += moves
        
        if arr[0] < arr[2]:
            print(-1)
        else:
            print(moves + (arr[0]-arr[2]))
        
    
