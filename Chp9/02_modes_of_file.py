# MODES OF OPENING A FILE

# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# 'rb' will open for read in binary mode.
# 'rt' will open for read in text mode

# Open the file in "w+" mode for writing and reading
f = open("file.txt", "w")

# Write some data to the file
f.write("Hello, World!")
f.close()  # Close the file

# Reopen the file in "r" mode for reading
f = open("file.txt", "r")

# Read the data from the file
data = f.read()
print(data)

# Close the file
f.close()

