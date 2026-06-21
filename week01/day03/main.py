from processor import FileProcessor
from utils import (
    file_exists,
    get_file_extension,
    get_filename_only,
    get_file_size,
)


def main():

    filename = "sample.txt"

    print(f"Exists: {file_exists(filename)}")
    print(f"Extension: {get_file_extension(filename)}")
    print(f"Filename: {get_filename_only(filename)}")

    processor = FileProcessor(filename)

    processor.load_file()

    print(f"File Size: {get_file_size(filename)} bytes")

    print(
        f"Content Length: "
        f"{processor.get_content_length()}"
    )

    processor.process_file()

    processor.save_file()


if __name__ == "__main__":
    main()

    
