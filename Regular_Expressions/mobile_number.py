import re


# [0-9]{10} means exactly 10 digits from 0 to 9.
pattern = r"[0-9]{10}"


# Test examples:
# Valid:   9876543210
# Invalid: 123456789, 98765A3210, 98765 43210
mobile_number = input("Enter a 10-digit mobile number: ")

if re.fullmatch(pattern, mobile_number):
    print("Valid mobile number.")
else:
    print("Invalid mobile number.")
