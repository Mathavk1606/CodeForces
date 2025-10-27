'''
Observations:
When all A's : It's always 1
When all B's : It's always query itself

6 4
BAABBA
2 8 32 95

for value 32
1cycle 
case B: 16
case A: 15 
case A : 14
case B : 7
case B : 4
case A : 3

2 cycle 
case B: 2
case A: 1
case A: 0
'''
for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    queries = list(map(int, input().split()))
    
    count_b = s.count('B')
    
    for query in queries:
        if count_b == 0:
            print(query)
            continue
        
        i = 0
        count = 0
        while query > 0:
            i = i % n
            if s[i] == 'B':
                query //= 2
            else:
                query -= 1
            count += 1
            i += 1
        print(count)