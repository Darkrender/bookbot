def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_map = get_character_map(text)

    print_book_report(book_path, word_count, char_map)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_map(text):
    lowered_text = text.lower()
    char_map = {}

    for char in lowered_text:
        if (char.isalpha()):
            char_map[char] = char_map.get(char, 0) + 1

    return char_map

def print_book_report(book_path, word_count, char_map):
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words were found in the document\n')

    char_map_list = sorted(char_map.items(), key=lambda kv: kv[1], reverse=True)
    for pair in char_map_list:
        print(f'The {pair[0]} character was found {pair[1]} times')

main()
