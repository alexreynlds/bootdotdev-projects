def get_num_words(book):
    words = book.split()
    return len(words)


def get_char_count(book):
    words = book.lower().split()
    raw_characters = list("".join(words))
    char_count = {}

    for char in raw_characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(items):
    return items["num"]


def sort_char_list(char_count):
    char_dicts = []

    for char in char_count:
        char_dicts.append({"char": char, "num": char_count[char]})

    char_dicts.sort(reverse=True, key=sort_on)
    return char_dicts
