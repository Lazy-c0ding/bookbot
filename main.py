def main():
    with open("books/frankenstein.txt") as f:
        file_contents =f.read()
        print("--- Begin report of books/frankenstein.txt ---")

def count():
    with open("books/frankenstein.txt") as f:
        file_contents =f.read()
    words = file_contents.split()
    count = len(words)
    print(f"{count} words found in the document")
    print("\n")
    return count

def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents =f.read()
    count_char = {}
    char_list = []
    for char in file_contents:
        lower = char.lower()
        if char.isalpha():
            if lower in count_char:
                count_char[lower] += 1
            else:
                count_char[lower] = 1
    for char, count in count_char.items():
        char_entry = {"letter": char, "num": count}
        char_list.append(char_entry)
    for item in char_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")
    return count_char


main()
count()
count_characters()
