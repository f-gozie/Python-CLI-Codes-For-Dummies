numbers = set(range(1,51))
set_3 = set()
for x in numbers:
    if x % 3 == 0:
        set_3.add( x)
        
print(set_3)

numbers = set(range(1,51))
set_2 = set()
for x in numbers:
    if x % 2 == 0:
        set_2.add( x)
        
print(set_2)

numbers = set(range(1,51))
set_5 = set()
for x in numbers:
    if x % 5 == 0:
        set_5.add( x)
        
print(set_5)
set2=(set_2-(set_3|set_5))
set3=(set_3-(set_2|set_5))
set5=(set_5-(set_2|set_3))
setx = (set2|set3|set5)
print(setx)
