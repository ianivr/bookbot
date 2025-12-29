from stats import get_num_words, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print(f"Found {get_num_words(get_book_text("books/frankenstein.txt"))} total words")

    result = get_char_count(get_book_text("books/frankenstein.txt"))
    print(result)


main()