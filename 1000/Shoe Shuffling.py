from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    
    freq_map = defaultdict(int)
    for i in s:
        freq_map[i] += 1
    
    flag = False 
    for count in freq_map.values():
        if count == 1:  
            flag = True
            break
    if flag:
        print(-1)
        continue
    
    students = list(range(1, n + 1))
    l, r = 0, 0 
    while r < n:
        if s[l] == s[r]:
            r += 1
        else:
            students[l:r] = students[l+1:r] + students[l:l+1]
            l = r
    
    students[l:r] = students[l+1:r] + students[l:l+1]
    print(' '.join(map(str, students)))