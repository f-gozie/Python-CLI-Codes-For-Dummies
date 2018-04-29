# The first letter varies from A to C
for first in 'ABC':
	for second in 'ABC':
		if second != first:
			for third in 'ABC':
				# Don't duplicate any letter
				if third != first and third != second:
					print(first + second + third)