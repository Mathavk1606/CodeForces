import sys

input = sys.stdin.read

data = input().split()

# Read the number of test cases
t = int(data[0])
index = 1

for _ in range(t):
	# Read the length of the string
	n = int(data[index])
	# Read the current color of the traffic light
	color = data[index + 1]
	# Read the traffic light color sequence
	s = data[index + 2]

	# Duplicate the string to simulate the cyclic nature of the traffic light
	s += s

	# Update n to reflect the new length of the duplicated string
	n *= 2

	# Initialize variables to track the last seen green light index and the maximum wait time
	last_green_index = -1
	max_seconds = -float('inf')

	# Traverse the string from the end to the beginning
	for i in range(n - 1, -1, -1):
		# Update the last seen green light index
		if s[i] == 'g':
			last_green_index = i

		# If the current color matches the given color, calculate the wait time
		if s[i] == color:
			difference = last_green_index - i
			# Update the maximum wait time
			max_seconds = max(max_seconds, difference)

	# Output the maximum wait time for the current test case
	print(max_seconds)

	index += 3

# Time Complexity (TC): O(n) = O(2*10^5)
# Space Complexity (SC): O(n) = O(2*10^5)
