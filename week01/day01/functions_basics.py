from pathlib import Path

def get_file_count(folder):
    return len(
        [
            file
            for file in Path(folder).iterdir()
            if file.is_file()
        ]
    )

def get_python_files(folder):
    return [
        file.name
        for file in Path(folder).iterdir()
        if file.suffix == ".py"
    ]

def main():
    folder = r"C:\Temp"
    count = get_file_count(folder)
    print(count)
    python_files = get_python_files(folder)
    print(python_files)
    

if __name__ == "__main__":
    main()
