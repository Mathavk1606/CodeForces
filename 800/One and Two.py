import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    #observations
    #find a point where no of 2's are same of both ends and return it's ind 
    #if no of 2's is zero, return 1 
    no_of_twos = a.count(2)
    current_no_of_twos = 0
    flag = True
    for i in range(n):
        if a[i] == 2: current_no_of_twos += 1
        
        if current_no_of_twos == (no_of_twos-current_no_of_twos):
            print(i+1)
            flag = False
            break
    if flag:
        print(-1)

            