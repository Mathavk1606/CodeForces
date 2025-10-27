import sys
data = sys.stdin.read().split()
idx = 0
t = int(data[idx])
idx += 1

for _ in range(t):
    n, p = int(data[idx]), int(data[idx+1])
    idx += 2
    a = list(map(int, data[idx:idx+n]))
    idx += n
    b = list(map(int, data[idx:idx+n]))
    idx += n
    
    cost = p
    notified = 1
    
    v = [(b[i],a[i]) for i in range(n)]
    v.sort()
    
    for shareCap,shareCost in v:
        if shareCost >= p:
            break
        
        if notified + shareCap > n:
            cost += (n-notified)*shareCost
            notified = n
            break
        else:
            cost += shareCap * shareCost
            notified += shareCap
    
    cost += (n-notified)*p
    print(cost)