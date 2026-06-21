import logging
from analyzer import FolderAnalyzer

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

def main():

    folder = "sample_data"

    analyzer = FolderAnalyzer(folder)

    file_count = analyzer.get_file_count()

    folder_count = analyzer.get_folder_count()

    largest_file = analyzer.get_largest_file()

    largest_size = analyzer.get_largest_file_size()

    print(
        f"Files: {file_count}"
    )

    print(
        f"Folders: {folder_count}"
    )

    print(
        f"Largest File: {largest_file}"
    )

    print(
        f"Largest Size: {largest_size} bytes"
    )


if __name__ == "__main__":
    main()

    


