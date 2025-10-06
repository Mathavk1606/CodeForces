t = int(input()) # Number of test cases

for _ in range(t):
	n = int(input()) 
	b = list(map(int, input().split(" "))) # Read the sequence b

	a = []
	a.append(b[0])
	for i in range(1, n):
		if b[i] >= b[i - 1]:
			a.append(b[i]) # If current element is greater than or equal to the previous, add it to a
		else:
			a.append(b[i]) # Add the current element to a
			a.append(b[i])

	print(len(a))
	print(' '.join(map(str, a)))