def alphabet_war(word):
    left_score = 0
    left_powers = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
    }

    right_score = 0
    right_powers = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1,
    }

    word = [i for i in word]
    for index, letter in enumerate(word):
        if letter == '*':
            try:
                word[index - 1] = '_'
            except IndexError:
                pass
            word[index] = '_'
        if word[index + 1] != '*':
            try:
                word[index + 1] = '_'
            except IndexError:
                pass

    for letter in word:
        if letter in left_powers:
            left_score += left_powers[letter]
        elif letter in right_powers:
            right_score += right_powers[letter]

    if left_score > right_score:
        return 'Left side wins!'
    elif right_score > left_score:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
