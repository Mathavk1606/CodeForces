t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    n, k, x = arr[0], arr[1], arr[2]
    ans = []

    if x != 1:
        ans = [1] * n
    else:
        if k >= 2:
            if n % 2 == 0:
                ans = [2] * (n // 2)
            else:
                if k >= 3:
                    ans = [3] + [2] * ((n - 3) // 2)
                else:
                    ans = []
        else:
            ans = []

    if sum(ans) == n:
        print("YES")
        print(len(ans))
        print(" ".join(map(str, ans)))
    else:
        print("NO")
