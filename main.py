from stats import number_of_words, count_chars,sort_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    letters_num = count_chars(text)
    nums = number_of_words(text)
    dict_sorted = sort_list(letters_num)
    pretty_print(book_path,nums,dict_sorted)

def get_book_text(filepath):
    with open (filepath) as f:
        return f.read()


def pretty_print(book_path,nums,dict_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {nums} total words")
    print("--------- Character Count -------")
    for item in dict_sorted:
        if not item["letter"].isalpha():
            continue
        print(f"{item['letter']}: {item['num']}")
    print("============= END ===============")

main()