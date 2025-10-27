import sys
from collections import defaultdict

input = sys.stdin.read

def main():
	data = input().split()
	t = int(data[0]) # Read the number of test cases
	index = 1
	results = []
	for _ in range(t):
		n = int(data[index]) # Read the size of the array for the current test case
		index += 1
		a = list(map(int, data[index:index + n])) # Read the elements of the array
		index += n

		frequency_map = defaultdict(int) # Dictionary to store frequency of each element
		for value in a:
			frequency_map[value] += 1 # Increment the frequency of the element

		current_highest_freq = 0
		for freq in frequency_map.values():
			current_highest_freq = max(current_highest_freq, freq) # Find the element with the highest frequency

		operations = 0 # Initialize the number of operations to zero
		while current_highest_freq < n: # Continue until the highest frequency is less than the size of the array
			operations += 1 # Increment operations for cloning the array
			if current_highest_freq * 2 <= n:
				operations += current_highest_freq # Add operations for swapping all the copies
				current_highest_freq *= 2 # Double the current highest frequency
			else:
				operations += n - current_highest_freq # Add operations for swapping only the required copies
				current_highest_freq = n # Set the highest frequency to the size of the array

		results.append(operations)

	for result in results:
		print(result) # Output the number of operations for each test case

if __name__ == "__main__":
	main()

# Time Complexity (TC): O(nlog2(n)) = O(10^5*log2(10^5)) = O(2*10^6)
# Space Complexity (SC): O(n) = O(10^5)
