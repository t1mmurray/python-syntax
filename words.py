def print_upper_words(list, letter):
    """Iterates through each list item and uppcases each letter in each word"""
    
    for word in list:
        if word.startswith(letter.lower()) or word.startswith(letter.upper()):
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "Ello"], "Y")