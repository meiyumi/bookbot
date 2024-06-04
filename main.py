def main():
    with open("books/frankenstein.txt") as f:
        frankenstein = f.read()
        # print(f.read())
        print(word_count(frankenstein))

def word_count(book):
    words = book.split()
    return len(words)

main()