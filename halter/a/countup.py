# Program that counts up from zero. The user continues the count by entering
# "Y". The user disconnects the count by entering "N"

import time

count = 0 # The current count
entry = "Y" # The count to begin with

while entry != "N" and entry != "n":
	# Print the value of the count
	print(count)
	entry = input("Please enter Y to continue or N to quit: ")
	if entry == "Y" or entry == "y":
		count += 1 # Keep counting
	# Check for bad entry
	elif entry != "N" and entry != 'n':
		print("" + entry )
		time.sleep(3)
		print(" is not a valid choice")
	# else must be "N" or "n"