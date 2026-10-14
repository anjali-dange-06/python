import re


# This pattern checks for a username, @, domain name, dot, and an
# extension containing at least two English letters.
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


# Test examples:
# Valid:   student.name@example.com, user123@mail.co
# Invalid: student.example.com, user@, user@example.c
email = input("Enter an email address: ")

if re.fullmatch(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")
