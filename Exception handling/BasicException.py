# Basic Exception Handling


# Main Program
def main():
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
    except ValueError:
        print("Please enter a valid whole number.")
    except ZeroDivisionError:
        print("The number cannot be zero.")
    else:
        print(f"10 divided by {number} is {result}")


if __name__ == "__main__":
    main()
