t = int(input())
for  _ in range(t):
    n,x = map(int,input().split(" "))
    nums = list(map(int,input().split(" ")))
    
    # "|=====|=====|"
    # "0     x    2x"
    
    #Using greedy
    nums.append(x)
    n = len(nums)
    
    max_distance_between_points = -float('inf')

    for i in range(1, n):
	    if i == n - 1:
		    max_distance_between_points = max(max_distance_between_points, 2 * (nums[i] - nums[i - 1]))
	    else:
		    max_distance_between_points = max(max_distance_between_points, nums[i] - nums[i - 1])

    print(max_distance_between_points)
    
   