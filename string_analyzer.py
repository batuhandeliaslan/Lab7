from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length

def main():
    sentence = input("Enter a sentence: ")

    capitalized = capitalize_words(sentence)
    reversed_str = reverse_string(sentence)
    cleaned = remove_punctuation(sentence)

    print("Capitalized:", capitalized)
    print("Reversed:", reversed_str)
    print("Character Count:", count_characters(cleaned))
    print("Word Count:", count_words(cleaned))
    print("Average Word Length:", average_word_length(cleaned))

if _name_ == "_main_":
    main()
