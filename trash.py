def compare (x,y):
    x=int(input("Enter an integer:"))
    y=int(input("Enter another integer:"))
    if x<y:
        print(x, "is less than", y)
    elif x>y:
        print(x, "is greater than", y)
    else:
        print(x, "and", y, "are equal")
        
compare(2,3)
compare(3,4)
compare(5,6)
          