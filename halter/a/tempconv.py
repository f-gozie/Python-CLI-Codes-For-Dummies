# File tempconv.py
# Author : Agozie Favour
# Last Modified : 21st August, 2017
# Converts degrees Fahrenheit to Celsius

# Prompt user for the temperature to convert and read the supplied value
degreesF = float(input("Enter the temperature in degrees F: "))

# Perform the Conversion
degreesC = 5/9*(degreesF - 32)

# Report the result
print(degreesF, "degrees F =", degreesC, 'degreesC')