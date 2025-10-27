'''
initially
m3 = 1 if (n-1)%2 == 0 or m3 = 2
m1 = m2 = (n-m3)//2 
'''
for _ in range(int(input())):
    n = int(input())
    m3 = 1 if (n-1)%2 == 0 else 2
    print((n-m3)//2)