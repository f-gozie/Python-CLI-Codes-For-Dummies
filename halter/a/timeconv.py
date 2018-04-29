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
print(hours, "hr,", minutes, "min, ", seconds, "sec.")