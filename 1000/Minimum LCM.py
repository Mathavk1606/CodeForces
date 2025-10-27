import math
for _ in range(int(input())):
    n = int(input())
    a = 1
    i = 2
    while i < math.sqrt(n)+1:
        if n%i == 0:
            a = n//i
            break
        i += 1
    print(a ," ", n-a)