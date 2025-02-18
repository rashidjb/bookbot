import re

def main():
    path_to_file = "books/frankenstein.txt"
    characters = {}


    with open(path_to_file) as f:
        file_contents = f.read()
        for letter in file_contents.lower():
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
        #print(characters)
        print("--- Begin report of books/frankenstein.txt --\n")
        print(f"{len(file_contents.split())} words found in the document\n")
        for character in characters:
            if re.match("[a-z]", character):
                print(f"The '{character}' character was found {characters[character]} times")
        print("--- End report ---")

main()