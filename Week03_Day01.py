#Series and Sequences
from calendar import calendar
print(calendar(2017))

'''n = int(input("Enter your number here: "))
x = 0
p = 0
while x < n:
    if x == 0:
        p += 0
    else:
        p = p + 100
    x += 1
print(p)
'''
def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num > 1:
        return fib(num-1) + fib(num - 2)
num = int(input("Number: "))
fib(num)