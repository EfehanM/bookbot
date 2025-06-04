def get_word_count(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lower_text = text.lower()
    char_counts = {}
    for ch in lower_text:
        if ch.isspace():
            continue
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
    return char_counts

    