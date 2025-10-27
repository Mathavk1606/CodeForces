for _ in range(int(input())):
    n = int(input())
    s = input()
    
    right_distinct = [0] * (n + 1)
    right_set = set()
    for i in range(n - 1, 0, -1):
        right_set.add(s[i])
        right_distinct[i] = len(right_set)
    
    max_sum = 0
    left_set = set()
    for i in range(n - 1):
        left_set.add(s[i])
        left_distinct = len(left_set)
        current_sum = left_distinct + right_distinct[i + 1]
        max_sum = max(max_sum, current_sum)
    
    print(max_sum)