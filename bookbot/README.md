# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## What it does

BookBot takes a book in `.txt` form and returns a word count along with the count of each alphabetical character in the book.

## Usage

```bash
python3 main.py <path_to_book>
```

## How it works

1. The user provides a file path to a book via a command-line argument. The program reads the file and returns it as a string.

2. The program splits the string into a list of words and returns the length of this list as the word count.

3. The string is converted to lowercase, split into words and then converted into a list of individual characters.

4. A dictionary is then created through looping through this list and checking to see if each character is present in the dictionary. If it isnt it's added and if it is then it's count value is incremented.

5. The dictionary is converted into a list of dictionaries and sorted by character count in descending order.

6. This sorted list along with the other results are then printed back to the user.
