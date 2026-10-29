# Custom Exception


# Custom Exception Class
class InvalidAgeError(Exception):
    pass


# Main Program
def main():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise InvalidAgeError("Age cannot be negative.")
    except ValueError:
        print("Please enter a valid whole number.")
    except InvalidAgeError as error:
        print(error)
    else:
        print(f"Your age is {age}.")


if __name__ == "__main__":
    main()
