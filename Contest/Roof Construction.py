import sys
import math

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) # Read the number of test cases
index += 1

for _ in range(t):
	n = int(data[index]) # Read the number of pillars
	index += 1
	n -= 1 # Decrement n to work with zero-based index
	msb = int(math.log2(n)) # Find the most significant bit position of n
	ans = [] # List to store the sequence of pillar heights
	num = (1 << msb) - 1 # Calculate the largest number with all bits set below msb
	while num >= 0: # Fill the list with numbers from num to 0
		ans.append(num)
		num -= 1

	num = 1 << msb # Start from the next power of 2
	while num <= n: # Fill the list with numbers from num to n
		ans.append(num)
		num += 1

	print(' '.join(map(str, ans))) # Output the sequence of pillar heights

# Time Complexity (TC): O(n) = O(2*10^5)
# Space Complexity (SC): O(n) = O(2*10^5)
