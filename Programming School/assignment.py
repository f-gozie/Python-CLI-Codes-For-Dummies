def divide(x, y):
	soln = x / y
	return soln

def add(x, y):
	soln = x + y
	return soln

def multiply(x, y):
	soln = x * y
	return soln


a = float(int(input("Enter first value: ")))
b = float(int(input("Enter second value: ")))

x = divide(a, b)
y = add(a, b)
z = multiply(a, b)

print("The addition of the two values is",int( y), "and their multiplication is",int( z), "with their division being", x)