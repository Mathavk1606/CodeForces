# Import necessary modules
import sys

# Read the number of players (n) and the power of the enemy team (d)
n, d = map(int, sys.stdin.readline().split())

# Read the power of each player
powers = list(map(int, sys.stdin.readline().split()))

# Sort the player powers in non-decreasing order
powers.sort()  # O(nlogn)

# Initialize pointers and counters
left = -1  # Pointer to track the leftmost player in the current team
right = n - 1  # Pointer to track the rightmost player in the current team
team_size = 1  # Current size of the team being formed
teams = 0  # Count of teams that can win

# Iterate until all players are considered
while left < right:  # O(n)
	if (powers[right] * team_size) <= d:
		left += 1
		team_size += 1
	else:
		teams += 1
		# Move the right pointer to form a new team
		right -= 1
		# Reset the team size for the new team
		team_size = 1

# Output the maximum number of winning teams
print(teams)

# Time Complexity (TC): O(nlogn) = O(10^5*log2(10^5)) = O(10^6)
# Space Complexity (SC): O(n)
