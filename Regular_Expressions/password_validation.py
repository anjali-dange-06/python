import re


# Lookaheads require an uppercase letter, lowercase letter, digit,
# and a non-whitespace special character. The final part requires
# at least 8 characters in total.
pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9\s]).{8,}"


# Test examples:
# Valid:   Hello@123, MyPass!7
# Invalid: hello@123, HELLO@123, Hello123, Hi@1
password = input("Enter a password: ")

if re.fullmatch(pattern, password):
    print("Valid password.")
else:
    print("Invalid password.")
