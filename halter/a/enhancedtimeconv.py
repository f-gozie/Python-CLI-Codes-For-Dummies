# Get the number of seconds
seconds = int(input("Please enter the number of seconds: "))
# Firstly, compute the number of hours in the given number of seconds
# Note: Integer division with possible truncation
hours = seconds//3600
# Then compute the number of seconds after the hours are accounted for
seconds = seconds % 3600
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
# Report the results
print(hours, ":", sep="", end="")
# Compute tens digits of minutes
tens = minutes // 10
# Compute ones digits of minutes
ones = minutes % 10
print(tens, ones, ":", sep="", end="")
# Compute tens digits of seconds
tens = seconds//10
# Compute ones digits of seconds
ones = seconds % 10
print(tens, ones, sep="")