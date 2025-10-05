import sys
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    
    frequency_map = Counter(a)

    if len(frequency_map) >= 3:  
	    print("No")  
    else:
	    freq_1 = next(iter(frequency_map.values()))
	    freq_2 = list(frequency_map.values())[-1]

	    if freq_1 == freq_2:  # If both frequencies are equal
		    print("Yes")  # The array can be made good
	    elif n % 2 == 1 and abs(freq_1 - freq_2) == 1:  # If the array length is odd and the frequency difference is 1
		    print("Yes")  # The array can be made good
	    else:
		    print("No")  # Otherwise, it's not possible
    