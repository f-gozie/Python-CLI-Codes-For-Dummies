fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    print(line.upper())
    count += 1

print("Line Count: ", count)
