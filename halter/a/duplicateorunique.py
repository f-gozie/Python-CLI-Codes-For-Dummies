print("Please enter five integer values.")
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))
d = int(input('Enter number 4: '))
e = int(input('Enter number 5: '))

if a == b or a == c or a == d or a == e:
	print("DUPLICATE")
if b == a or b == c or b == d or b == e:
	print("DUPLICATE")
if c == b or c == a or c == d or c == e:
	print("DUPLICATE")
if d == a or d == b or d == c or d == e:
	print("DUPLICATE")
if e == a or e == b or e == c or e == d:
	print("DUPLICATE")