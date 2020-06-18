# pysearch.py

import argparse
import pathlib


def search_folder(path, extension, file_size=None):
    """
    Search folder for files
    """
    folder = pathlib.Path(path)
    files = list(folder.rglob(f'*.{extension}'))

    if not files:
        print(f'No files found with {extension=}')
        return

    if file_size is not None:
        files = [f for f in files
                 if f.stat().st_size > file_size]

    print(f'{len(files)} *.{extension} files found:')
    for file_path in files:
        print(file_path)


def main():
    parser = argparse.ArgumentParser(
        'PySearch',
        description='PySearch - The Python Powered File Searcher')
    parser.add_argument('-p', '--path',
                        help='The path to search for files',
                        required=True,
                        dest='path')
    parser.add_argument('-e', '--ext',
                        help='The extension to search for',
                        required=True,
                        dest='extension')
    parser.add_argument('-s', '--size',
                        help='The file size to filter on in bytes',
                        type=int,
                        dest='size',
                        default=None)

    args = parser.parse_args()
    search_folder(args.path, args.extension, args.size)

if __name__ == '__main__':
    main()