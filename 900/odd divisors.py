for _ in range(int(input())):
    n = int(input())
    while n % 2 == 0:
        n //= 2
    
    if n>1:
        print("Yes")
    else:
        print("No")