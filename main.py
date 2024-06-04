def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        frankenstein = f.read()
        # print(f.read())
        words = word_count(frankenstein)
        # print(character_count(frankenstein))
        
        sorted_list = sorter(character_count(frankenstein))
        print(f"--- Begin report of {book_path} ---")
        print(f"{words} words found in the document")
        print()

        for a in sorted_list:
            print(f"The '{a['char']}' character was found {a['num']} times")
        print("--- End report ---")


def word_count(book):
    words = book.split()
    return len(words)

def character_count(book):
    count = {}
    book_lowercase = book.lower()
    
    for letter in book_lowercase:
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
            
    return count

def sort_on(dict):
    return dict["num"]

def sorter(char_count):
    char_list = []
    for char in char_count:
        char_dict = {
            "char": char,
            "num": char_count[char]
        }
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()