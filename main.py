import sys

from stats import get_num_chars, get_num_words, sort_results


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    title = "=" * 12 + " " + "BOOKBOT" + " " + "=" * 12
    print(title)
    print(f"Analyzing book found at {path}...")
    wc_title = "-" * 11 + " Word Count " + "-" * 11
    print(wc_title)
    print(f"Found {num_words} total words")
    ch_title = "-" * 11 + " Character Count " + "-" * 11
    print(ch_title)
    num_chars = get_num_chars(book_text)
    sorted_num_chars = sort_results(num_chars)
    for c in sorted_num_chars:
        print(f"{c['char']}: {c['num']}")
    end_title = "=" * 12 + " END " + "=" * 12
    print(end_title)


def get_book_text(path):
    with open("./" + path) as f:
        file_contents = f.read()
    return file_contents


main()
