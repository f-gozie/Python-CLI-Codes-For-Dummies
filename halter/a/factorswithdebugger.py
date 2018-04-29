MAX = 20
n = 1

while n <= MAX:
	factor = 1
	print(end = str(n)  +  ': ')
	while factor <= n:
		print('factor =', factor, ' n =', n)
		if n % factor == 0:
			print(factor, end=' ')   # If so, display it
			factor += 1
	print() # Move to next line for next n
	n += 1