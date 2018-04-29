letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
print(letter_counts)

for letter in letter_counts:
    print(letter,'|','*' * letter_counts[letter])
