name = input("Enter the file name: ")
text = open(name)
count = 0
for line in text:
    if line.startswith("Subject"):
        count += 1
print("There were ", count, "subject lines in ", name)
