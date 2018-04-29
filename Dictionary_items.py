#create a list
l = ['rabbt', 'frequency']
def a(l):
    x = l
    min = x[0]
    for index, a in enumerate(l):
        if a[1] < min [1]:
            min = a
        print(min)
    return (index, min)


sorted_dict = []
for item in l:
    index, min = a(l)
    l.pop(index)
    sorted_dict.append(min)
print(sorted_dict)