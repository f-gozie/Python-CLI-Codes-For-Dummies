l=['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1,2,3]]

for item in l:
    if type(item) == list:
        print("It's a list")
        for i in item:
            print(i)
    else:
        print(item)

print(len(l))
print(len(item))
