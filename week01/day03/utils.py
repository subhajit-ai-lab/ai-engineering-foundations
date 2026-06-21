from pathlib import Path


def file_exists(filename):
    return Path(filename).exists()


def get_file_extension(filename):
    return Path(filename).suffix


def get_filename_only(filename):
    return Path(filename).name


def get_file_size(filename):
    return Path(filename).stat().st_size

