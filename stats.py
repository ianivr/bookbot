def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_counter = {}
    for char in text:
        lowerChar = char.lower()
        if lowerChar in char_counter:
            char_counter[lowerChar] += 1
        else:
            char_counter[lowerChar] = 1
    
    return char_counter

def get_sorted_dictionary(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        chars_list.append({
            "char": char,
            "num": count
        })

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(dict_item):
    return dict_item["num"]

def remove_non_alpha_chars(chars_list):
    new_list = []
    for item in chars_list:
        if item["char"].isalpha():
            new_list.append(item)
    
    return new_list

def get_formated_list(old_list):
    formated_string = ""

    for item in old_list:
        if not formated_string:
            formated_string += f"{item["char"]}: {item["num"]}"
        else:
            formated_string += f"\n    {item["char"]}: {item["num"]}"

    return formated_string