s = "ABCDEFGHIJK"
print(s)
for i in range(len(s)):
    print("[", s[i], "]", sep="", end="")
print()  # Print a new line
for ch in s:
    print("<", ch, ">", sep="", end="")
print()
