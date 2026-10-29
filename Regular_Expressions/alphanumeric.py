import re


# [A-Za-z0-9]+ allows one or more English letters or digits.
pattern = r"[A-Za-z0-9]+"


# Test examples:
# Valid:   Python123, A1B2
# Invalid: two words, Python!, A-1
text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("The string contains only English alphabets and digits.")
else:
    print("The string contains other characters.")
