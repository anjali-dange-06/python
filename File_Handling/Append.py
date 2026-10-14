from pathlib import Path


# File Path
file_path = Path(__file__).with_name("sample.txt")


# Main Program
def main():
    with file_path.open("a", encoding="utf-8") as file:
        file.write("This line was added using append mode.\n")

    print(f"Text appended to {file_path.name}")


if __name__ == "__main__":
    main()
