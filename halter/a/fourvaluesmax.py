# # Get input from the user
# print("Please enter four integer values.")
# a = int(input('Enter number 1: '))
# b = int(input('Enter number 2: '))
# c = int(input('Enter number 3: '))
# d = int(input('Enter number 4: '))

# # Compute the maximum value
# if a >= b and a >= c and a >= d:
# 	max = a
# elif b >= a and b >= c and b >= d:
# 	max = b
# elif c >= b and c >= a and c >= d:
# 	max = c
# elif d >= b and d >= c and d >= a:
# 	max = d

# # Report the result
# print("The maximum number entered was: ", max)

# OR

# Get input from the user
print("Please enter four integer values.")
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))
d = int(input('Enter number 4: '))

# Compute the maximum value
max = a
if b > max:
	max = b
elif c > max:
	max = c
elif d > max:
	max = d
	
# # Report the result
print("The maximum number entered was: ", max)