# Try, Except, Else, and Finally


# Main Program
def main():
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Please enter a valid whole number.")
    else:
        print(f"You entered {number}.")
    finally:
        print("Program finished.")


if __name__ == "__main__":
    main()
