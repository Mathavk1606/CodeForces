t = int(input())
for _ in range(t):
    n = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    print(sum(arr)*-1)