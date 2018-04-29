# Program to count the number of integers in a string
word = input("Enter Text: ")
vowel_count = 0
for x in word:
	if x == "A" or x == "a" or x == "I" or x == "i" or x == "O" or x == "o" or x == "U" or x == "u" \
	or x == "E" or x == "e":
		print(x, ', ', sep="", end="")
		vowel_count += 1
print(' (', vowel_count, ' vowels)', sep="")