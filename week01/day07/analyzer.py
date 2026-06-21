from pathlib import Path
import logging

class FolderAnalyzer:

    def __init__(self, folder_path: str):

        self.folder_path = Path(folder_path)


    def get_file_count(self) -> int:

        return len(
            [
                file
                for file in self.folder_path.rglob("*")
                if file.is_file()
            ]
        )


    def get_folder_count(self) -> int:

        return len(
            [
                folder
                for folder in self.folder_path.rglob("*")
                if folder.is_dir()
            ]
        )


    def get_largest_file(self):

        files = [
            file
            for file in self.folder_path.rglob("*")
            if file.is_file()
        ]

        if not files:
            return None

        return max(
            files,
            key=lambda file: file.stat().st_size
        )


    def get_largest_file_size(self) -> int:

        largest = self.get_largest_file()

        if largest is None:
            return 0

        return largest.stat().st_size


