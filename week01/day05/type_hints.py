from pathlib import Path


def process_file(path: str) -> list:

    file_path = Path(path)

    if not file_path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return lines


def count_words(text: str) -> int:
    return len(text.split())


def get_file_extension(
    filename: str
) -> str:
    return Path(filename).suffix


def main():

    lines = process_file("sample.txt")

    print(lines)

    print(
        count_words(
            "AI Engineering is fun"
        )
    )

    print(
        get_file_extension(
            "report.pdf"
        )
    )


if __name__ == "__main__":
    main()


    
