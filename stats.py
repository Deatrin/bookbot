def get_word_count(filepath):
    book = get_book_text(filepath)
    split = book.split()
    c = 0
    for split in split:
        c += 1
    return c
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content


def get_char_count(file_path):
    char_freq = {}
    word_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    # Count words
    word_count = len(text.split())

    # Count characters
    for char in text:
        if char.isalpha():  # only alphabetic characters
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

    # Sort character counts by descending frequency
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    return {
        "word_count": word_count,
        "char_counts": sorted_chars
    }