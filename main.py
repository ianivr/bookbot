from stats import get_num_words, get_char_count, get_sorted_dictionary, remove_non_alpha_chars, get_formated_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    result = get_char_count(book)
    chars_list = get_sorted_dictionary(result)
    new_list = remove_non_alpha_chars(chars_list)
    formated_list = get_formated_list(new_list)

    string_structure = f"""
    ============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {get_num_words(book)} total words
    --------- Character Count -------
    {formated_list}
    ============= END ===============
    """

    print(string_structure)

main()