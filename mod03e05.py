def function_a():
    print("function_a was called")
def function_b():
    print("function_b was called")
def function_c():
    print("function_c was called")    
def dispatch(choice):
    True or False
    True and False
    not(False) and True
    True or 7
    False or 7
    True and 0
    False or 8
    "happy" and "sad"
    "happy" or "sad"
    "" and "sad"
    "happy" and ""
    
    choice = input("Select an option from a, b and c: ")
    if choice == 'a':
        function_a()
    elif choice == 'b':
        function_b()
    elif choice == 'c':
        function_c()
    else:
        print("Invalid Choice!!!")
dispatch('')
        
    