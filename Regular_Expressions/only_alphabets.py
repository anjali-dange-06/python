import re


# [A-Za-z]+ means one or more English uppercase or lowercase letters.
pattern = r"[A-Za-z]+"


# Test examples:
# Valid:   Hello, Python
# Invalid: Hello123, two words, hello!
text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("The string contains only English alphabets.")
else:
    print("The string does not contain only English alphabets.")
