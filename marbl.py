import sys
import re

def marbl_vowels(word):
    marbled_word = ""
    for i, letter in enumerate(word):
        if i == 0 or letter.lower() in 'vrbthlxsmn' or not letter.isalpha():
            marbled_word += letter
        elif letter.lower() in 'aeiou':
            marbled_word += 'x'
        else:
            marbled_word += 'x'

    if word[-1].lower() not in 'aeiou' and word[-1].isalpha():
        marbled_word = marbled_word[:-1] + word[-1]
    return marbled_word

def marbl_word(match):
    word = match.group()
    if len(word.strip()) <= 2:
        return word
    else:
        return marbl_vowels(word)

def marbl_string(text):
    return re.sub(r'\b\w+\b', marbl_word, text)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to marbl.")
        sys.exit(1)

    input_text = sys.argv[1]
    marbled_text = marbl_string(input_text)
    print(marbled_text)

if __name__ == "__main__":
    main()

