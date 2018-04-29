# Get input from the user
print("Please enter five integer values.")
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))
d = int(input('Enter number 4: '))
e = int(input('Enter number 5: '))

max = a
min = a
if b > max:
	max = b
elif min > b:
	min = b

if c > max:
	max = c
elif min > c:
	min = c

if d > max:
	max = d
elif min > d :
	min = d	

if e > max:
	max = e
elif min > e:
	min = e	

print("Your minimum value is ", min, " and your maximum value is ", max)