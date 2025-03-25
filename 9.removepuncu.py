# String with punctuations
input_string = "Hello, world! Welcome to the exciting world of Python programming."

# List of punctuations to be removed
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Removing punctuations from the string
cleaned_string = ""
for char in input_string:
    if char not in punctuations:
        cleaned_string += char

# Print the string without punctuations
print("Original String:", input_string)
print("String without punctuations:", cleaned_string)
