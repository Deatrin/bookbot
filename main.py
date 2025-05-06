from stats import get_char_count
import sys




def main():
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    stats = get_char_count(filepath)

    print("----------- Word Count ----------")
    print(f"Found {stats['word_count']} total words")

    print("--------- Character Count -------")
    for char, count in stats['char_counts']:
        print(f"{char}: {count}")

    print("============= END ===============")

try:
    main()
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)