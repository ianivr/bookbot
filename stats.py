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