# Determine the character count of each letter from a string of text.
print("Enter text: ")
text = input()
count = {}

for character in text:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print("Char count: " + str(count))
