from pathlib import Path


# File Path
file_path = Path(__file__).with_name("sample.txt")


# Main Program
def main():
    try:
        with file_path.open("r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("sample.txt was not found. Run Write.py first.")
        return

    print("File contents:")
    print(content, end="")


if __name__ == "__main__":
    main()
