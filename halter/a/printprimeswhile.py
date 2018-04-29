from math import sqrt

max_value = int(input("Display primes up to what value? "))
value = 2

while value <= max_value:
	# See if value is prime
	is_prime = True
	trial_factor = 2
	root = sqrt(value)
	while trial_factor < root:
		is_prime = (value % trial_factor != 0)
		trial_factor += 1
	if is_prime:
		print(value, end=', ')
	value += 1
print()