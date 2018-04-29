# acquire a number from a user and print its absolte value

n = int(input("Enter a number: "))
print('|', n, '| = ', (n if n >= 0 else -n), sep='')