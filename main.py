def main():
    with open("books/frankenstein.txt") as f:
        frankenstein = f.read()
        # print(f.read())
        # print(word_count(frankenstein))
        print(character_count(frankenstein))

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

main()