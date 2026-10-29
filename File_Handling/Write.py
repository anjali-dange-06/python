from pathlib import Path


# File Path
file_path = Path(__file__).with_name("sample.txt")


# Main Program
def main():
    with file_path.open("w", encoding="utf-8") as file:
        file.write("Hello! This is a file handling example.\n")
        file.write("This text was written to the file.\n")

    print(f"Text written to {file_path.name}")


if __name__ == "__main__":
    main()
