# The best way to open and close the file automatically is the with statement.

# Open the file in read mode using 'with', which automatically closes the file
with open("file.txt", "r") as f:
    # Read the contents of the file
    data = f.read()
    # Print the contents
    print(data)
