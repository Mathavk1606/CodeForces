t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxLen = 0
    i, j = 0, 0
    while j < n:
        if arr[j] == 1:
            maxLen = max(maxLen, j - i)
            i = j + 1
        j += 1
    maxLen = max(maxLen, j - i)
    print(maxLen)
