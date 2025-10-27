'''
Eat only
|v - ai | <= x
v lies in the interval [ai - x, ai + x]

8 2
2 7 8 9 6 13 21 28

[0,4]
[5,9]
[6,10]
[7,11]
[4,8]
[11,15]
[19,23]
[26,30]

Nothing but overlaps are found and subtracted with n

'''

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    intervals = [[a - x, a + x] for a in arr]
    
    overlaps = 0
    for i in range(n-1):
        if intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[i+1][0]:
            overlaps += 1
    
    print(n - overlaps)