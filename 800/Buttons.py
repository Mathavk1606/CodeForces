t = int(input())
for _ in range(t):
    arr = list(map(int,input().split(" ")))
    a = arr[0]
    b = arr[1]
    if arr[-1]%2 == 0:
        if a > b:
            print("First")  # Katie wins
        else:
            print("Second")  # Anna wins
    else:
        if b > a:
            print("Second")  # Katie wins
        else:
            print("First")  # Anna wins