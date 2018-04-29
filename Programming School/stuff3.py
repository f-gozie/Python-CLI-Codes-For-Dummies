#enumerate generates index and value


numbers=list(range(2,31))
prime=numbers[:]
for number in numbers:
    for digit in numbers:
        if number % digit==0 and number!=digit:
            if number in prime:
                prime.remove(number)
print(prime)