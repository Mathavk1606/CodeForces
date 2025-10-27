for _ in range(int(input())):
    n = int(input())
    minValue = float('inf')
    secondValues = []
    for i in range(n):
        m = int(input())
        tmp = list(map(int,input().split(" ")))
        tmp.sort()
        minValue = min(minValue,tmp[0])
        secondValues.append(tmp[1])
    secondValues.sort()
    
    print(minValue + sum([secondValues[i] for i in range(n-1,0,-1)]))

    
    