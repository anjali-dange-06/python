# FILE HANDLING IN PYTHON

# CREATE FILE
def create_file():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "x")
        file.close()
        print("File created successfully")

    except FileExistsError:
        print("File already exists")


# READ FILE
def read_file():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")

        data = file.read()
        print("\nFile content:")
        print(data)

        file.close()

    except FileNotFoundError:
        print("File not found")


# WRITE FILE
def write_file():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "w")

        data = input("Enter data to write: ")
        file.write(data)

        file.close()

        print("Data written successfully")

    except FileNotFoundError:
        print("File not found")


# APPEND FILE
def append_file():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "a")

        data = input("Enter data to append: ")
        file.write("\n" + data)

        file.close()

        print("Data appended successfully")

    except FileNotFoundError:
        print("File not found")


# DELETE FILE
def delete_file():
    filename = input("Enter file name: ")

    try:
        import os

        os.remove(filename)

        print("File deleted successfully")

    except FileNotFoundError:
        print("File not found")


# MAIN PROGRAM

while True:

    print("\n===== FILE OPERATIONS =====")
    print("1. Create File")
    print("2. Read File")
    print("3. Write File")
    print("4. Append File")
    print("5. Delete File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        read_file()

    elif choice == "3":
        write_file()

    elif choice == "4":
        append_file()

    elif choice == "5":
        delete_file()

    elif choice == "6":
        print("Program ended")
        break

    else:
        print("Invalid choice")

    #1. What is File Handling? 
    #2. Why Do We Need File Handling?
    #3. Types of Files
    #4. Opening a File
    #5. open() Function
    #6. File Modes
    #7. r — Read Mode
    #8. w — Write Mode
    #9. a — Append Mode
    #10. x — Create Mode
    #11. The Most Important Mode Comparison
    #12. read()
    #13. readline()
    #14. readlines()
    #15. read() vs readline() vs readlines()
    #16. write()
    #17. writelines()
    #18. write() vs writelines()
    #19. Closing a File
    #20. with open()
    #21. File Pointer
    #22. tell()
    #23. seek()
    #24. Basic Exceptions
    #25. Important File Exceptions
