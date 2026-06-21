from pathlib import Path


class FileProcessor:
    """
    Simple file processor used to demonstrate:
    - Classes
    - Objects
    - Instance variables
    - Methods
    """

    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def load_file(self):
        """
        Load file content into memory.
        """

        file_path = Path(self.filename)

        if not file_path.exists():
            print(f"File not found: {self.filename}")
            return

        with open(file_path, "r", encoding="utf-8") as file:
            self.content = file.read()

        print(f"Loaded file: {self.filename}")

    def process_file(self):
        """
        Simple processing example:
        Convert content to uppercase.
        """

        if not self.content:
            print("No content loaded.")
            return

        self.content = self.content.upper()

        print("File content processed.")

    def save_file(self):
        """
        Save processed content to a new file.
        """

        if not self.content:
            print("Nothing to save.")
            return

        output_file = f"processed_{Path(self.filename).name}"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self.content)

        print(f"Saved processed file as: {output_file}")

    def get_filename(self):
        """
        Return filename.
        """

        return self.filename

    def get_content_length(self):
        """
        Return number of characters in loaded content.
        """

        return len(self.content)


def main():
    processor = FileProcessor("sample.txt")

    print(f"Filename: {processor.get_filename()}")

    processor.load_file()

    print(
        f"Content Length: "
        f"{processor.get_content_length()} characters"
    )

    processor.process_file()

    processor.save_file()


if __name__ == "__main__":
    main()

