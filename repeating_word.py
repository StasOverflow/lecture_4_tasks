text = (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
        'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris' 
        'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in' 
        'reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.' 
        'Excepteur sint occaecat cupidatat non proident,' 
        'sunt in culpa qui officia deserunt mollit anim id est laborum.'
        )


def find_most_used(some_text):
    word_dict = {}
    max_value = 0
    repeating_words = []

    some_text = some_text.split()

    print(some_text)

    for s in some_text:
        s = s.lower()       
        word_dict[s] = word_dict.get(s, 0) + 1

    for key in word_dict:
        if max_value < word_dict[key]:
            repeating_words.append(key)
            max_value = word_dict[key]

    print('\nWe have these word(s)', ', '.join(repeating_words), 'repeating', max_value, 'times')


find_most_used(text)
