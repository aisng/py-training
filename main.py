import os
import argparse
import re
from typing import Generator


def main() -> None:
    parser = argparse.ArgumentParser(description="grep with Python")
    parser.add_argument("pattern", type=str, help="Pattern to search")
    parser.add_argument("-E", "--extended-regexp", action="store_true")
    args = parser.parse_args()

    pattern_to_search = args.pattern
    is_regex_pattern = args.extended_regexp
    dir_list = os.listdir()

    for item in dir_list:
        if not os.path.isfile(item):
            continue
        result_gen = search_pattern(
            pattern=pattern_to_search, file=item, is_regex=is_regex_pattern
        )
        try:
            while True:
                search_val = next(result_gen)
                print(search_val.strip())
        except StopIteration:
            pass


def search_pattern(pattern: str, file: str, is_regex: bool) -> Generator[str, str, str]:

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

        if is_regex:
            for line in file_data:
                match = re.search(pattern, line)
                if match is None:
                    continue
                yield line
        else:
            for line in file_data:
                if not pattern in line:
                    continue
                yield line


if __name__ == "__main__":
    main()
