n = int(input("how many numbers are you working with? "))
def addit(n):
	total = 0
	for i in range(0,n):
		a = int(input("Please enter a number "))
		total = total + a
	print("The sum of all these numbers is", total)
def multiplyit(n):
	total = 1
	for i in range(0,n):
		a = int(input("Please enter a number ",)) 
		total = total * a
	print("The multiplication of all these numbers ",total)

def maximum(n):
	list1 = []	
	for i in range(0,n):
		x = int(input("Put in your number "))
		list1.append(x)
	highest = max(list1)
	print(highest)

def factorial(n):
	for i in range(1,n):
		n *= i
	print(n)
factorial(n)

