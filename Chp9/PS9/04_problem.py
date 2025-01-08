# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
# Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "burdens"]

# Read the file content
with open("file.txt") as f:
    content = f.read()

# Replace each word in the list with censored text
for word in words:
    content = content.replace(word, "#" * len(word))

# Write the updated content back to the file
with open("file.txt", "w") as f:
    f.write(content)
