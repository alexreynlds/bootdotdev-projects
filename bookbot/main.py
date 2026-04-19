from stats import get_num_words, get_char_count, sort_char_list
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents


def print_report(book_dir, word_count, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_dir}")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    for char in sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_dir = sys.argv[1]

    book = get_book_text(book_dir)
    word_count = get_num_words(book)
    char_list = get_char_count(book)
    sorted = sort_char_list(char_list)

    print_report(book_dir, word_count, sorted)

    # print(f"Found {get_num_words(book)} total words")


if __name__ == "__main__":
    main()
