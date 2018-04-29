from time import clock

max_value = int(input("Display primes up to what value? "))
count = 0
start_time = clock()

for value in range(2, max_value+1):
	is_prime = True
	for trial_factor in range(2, value):
		if value % trial_factor == 0:
			is_prime = False
			break
	else:
		print(value, end=" ")
		count += 1
print()
elapsed = clock() - start_time
print("Count: ", count, "Elapsed time: ", elapsed)