import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arrSet = set(arr)
    
    global_gcd = arr[0]
    for i in range(1, n):
        global_gcd = math.gcd(global_gcd, arr[i])
        if global_gcd == 1:
            break
    
    for p in primes:
        if global_gcd % p != 0:
            print(p)
            break
    
    