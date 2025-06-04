from stats import get_word_count, get_num_chars
import sys

# Reads the entire contents of the book at the given file path
# Returns the text as a string
# If the file does not exist, an exception will be raised

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_sentence_count(text):
    sentences = text.split(".")
    return len(sentences)

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_counts = get_num_chars(book_text)
    print("============ BOOKBOT ============")
    print(f"--- Analyzing book found at {book_path} ---")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(f"Character counts:")
    for char in sorted(char_counts):
        print(f"{char}: {char_counts[char]}")
    print("============= END ===============")

main() 