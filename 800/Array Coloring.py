t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    arr.sort()
    for i in range(0,len(arr)-1):
        sum1 = sum(arr[:i+1])
        sum2 = sum(arr[i+1:])
        if sum1 %2 == sum2%2:
            print("Yes")
            break
        if i == len(arr)-2:
            print("No")
    
    