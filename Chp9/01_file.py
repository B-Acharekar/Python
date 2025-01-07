# A file is data stored in a storage device. 
# A python program can talk to the file by reading content from it and writing content to it.
# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)

# Python has an open() function for opening files. It takes 2 parameters: filename and
# mode.
# open("filename", "mode of opening(read mode by default)")
f = open("file.txt", "r")

# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()

f.readline() # Read one line from the file.

