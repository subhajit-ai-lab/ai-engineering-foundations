from pathlib import Path


class FileProcessor:

    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def load_file(self):

        file_path = Path(self.filename)

        if not file_path.exists():
            print(f"File not found: {self.filename}")
            return

        with open(file_path, "r", encoding="utf-8") as file:
            self.content = file.read()

        print(f"Loaded file: {self.filename}")

    def process_file(self):

        if not self.content:
            print("No content loaded.")
            return

        self.content = self.content.upper()

        print("File content processed.")

    def save_file(self):

        if not self.content:
            print("Nothing to save.")
            return

        output_file = f"processed_{Path(self.filename).name}"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self.content)

        print(f"Saved file: {output_file}")

    def get_filename(self):
        return self.filename

    def get_content_length(self):
        return len(self.content)

    
