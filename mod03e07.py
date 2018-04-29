def is_divisible_by_n(x, n):

    
    if n % x == 0:
        print(x, "is divisible by", n)
    else:
        print(x, "is not divisible by", n)
is_divisible_by_n(10, 4)