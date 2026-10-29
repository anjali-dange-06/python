import re


# [A-Za-z0-9_]{3,} allows English letters, digits, and underscores,
# with a minimum length of 3 characters.
username_pattern = r"[A-Za-z0-9_]{3,}"

# Lookaheads require uppercase, lowercase, digit, and non-whitespace
# special character; .{8,} requires at least 8 characters in total.
password_pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9\s]).{8,}"


# Test examples:
# Valid username:   student_1
# Invalid username: ab, user name, name!
# Valid password:   College@123
# Invalid password: college@123, COLLEGE@123, College123
username = input("Enter a username: ")
password = input("Enter a password: ")

if re.fullmatch(username_pattern, username):
    print("Username is valid.")
else:
    print("Username is invalid.")

if re.fullmatch(password_pattern, password):
    print("Password is valid.")
else:
    print("Password is invalid.")
