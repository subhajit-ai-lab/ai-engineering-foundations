import logging
from pathlib import Path


logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)


def process_file(path: str) -> list:

    logging.info(
        f"Processing {path}"
    )

    file_path = Path(path)

    if not file_path.exists():

        logging.error(
            f"{path} not found"
        )

        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

    logging.info(
        f"{len(lines)} lines loaded"
    )

    return lines


def main():

    logging.info(
        "Program started"
    )

    process_file(
        "sample.txt"
    )

    process_file(
        "missing.txt"
    )

    logging.info(
        "Program finished"
    )


if __name__ == "__main__":
    main()

