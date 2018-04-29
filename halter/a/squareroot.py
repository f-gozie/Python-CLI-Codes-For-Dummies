# Get value from user
val = float(input("Enter Value: "))

# Compute a provisional square root
root = 1.0

# How far off is the provisional square root
diff = root*root - val

# Loop until the provisional root is close enough to the actual root
while diff > 0.00000001 or diff < -0.00000001:
	print(root, 'squared is', root*root)  # Report how we are doing
	root = (root + val/root) / 2  # Compute new provisional root

	# How bad is our approximation
	diff = root*root - val

# Report approximate square root
print('Square root of ', val, '=', root)