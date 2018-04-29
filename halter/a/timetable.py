# Get the numbers of rows and columns in the table
size = int(input("Enter the table size: "))
# Print a size x size multiplication table
# First, print heading: 1 2 3 4 5 etc.
print("     ", end="")
# Print column heading
for column in range(1, size+1):
	print("{0:4}".format(column), end="")  # Display column number
print() # Go down to the next line
# Print line separator +--------------
print("    +", end="") # Display line
for column in range(1, size+1):
	print("----", end="")
print()

# Print table contents 
for row in range(1, size+1):
	print("{0:3} |".format(row), end="")
	for column in range(1, size+1):
		product = row*column
		print("{0:4}".format(product), end='')
	print()