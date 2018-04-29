#program to find the second smallest number in a list
value = [8,2,4,6,9]
def second_minimum_number(value):
    min = value[0]
    previous = value[1]
    for a in value:
        if a < min:
            previous = min
            min = a
    return previous
print(second_minimum_number(value))
             
        
            