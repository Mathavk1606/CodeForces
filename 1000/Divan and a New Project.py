for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    ans = [0] * (n + 1)  
    
    altA = [(a[i], i) for i in range(n)]
    altA.sort(reverse=True)
    
    cost = 0
    coord = 1
    for (val, ind) in altA:
        ans[ind + 1] = coord
        cost += (2 * abs(coord) * val)  # Fixed: use val and abs(coord)
        if coord < 0:
            coord = abs(coord) + 1
        else:
            coord = -coord
    print(cost)
    print(' '.join(map(str, ans)))  # Fixed: space-separated output