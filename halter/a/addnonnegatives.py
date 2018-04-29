''' Allow the user to enter a sequence of non negative integers. The
user ends the list with a negative integer. At the end of the program, the sum
of non negative numbers entered is displayed. The program prints zero if the user provides no non negative numbers
'''
entry = 0 # Ensure the loop is entered
sum = 0 # Initialize sum

# Request input from the user
print("Enter numbers to sum, negative numbers end list")

while True:
	entry = int(input("Value: "))
	if entry < 0:
		break
	sum += entry
print("Sum =", sum)