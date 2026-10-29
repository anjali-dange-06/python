import re


# [0-9]+ means one or more ASCII digits and nothing else.
pattern = r"[0-9]+"


# Test examples:
# Valid:   12345, 007
# Invalid: 12A45, 12 45, 12.45
text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
