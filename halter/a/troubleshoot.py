# Program to troubleshoot a faulty computer
print("Oh! Almighty Agozie, help me, my computer is fucking with me")
done = False # Problem not solved initially

while True:
	print("Does the computer make any sounds (fans, e.t.c.)")
	choice = input("Or show any lights? (y/n):")
	# The troubleshooting control logic
	if choice == 'n':
		choice = input("Is it plugged in? (y/n):")
		if choice == 'n':
			print("Plug it in.")
		else:
			choice = input("Is the switch in the 'on' position? (y/n):")
			if choice == "n":
				print("Turn it on")
			else:
				choice = input("Does the computer have a fuse? (y/n):")
				if choice ==  "n":
					choice = input("Is the outlet OK? (y/n)")
					if choice == "n":
						print('''Check the outlet's circuit breaker or fuse.
								Move to a new outlet, if necessary.''')
					else:
						print("Please consult a service technician")
						break
				else:
					print("Check fuse. Replace if necessary.")
	else:
		print("Please consult a service technician")
		break