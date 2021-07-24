VALUES = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'
}


def encode(st):
    word = ''
    for letter in st:
        if letter in VALUES:
            word += VALUES[letter]
        else:
            word += letter
    return word


def decode(st):
    word = ''
    for letter in st:
        if letter in VALUES.values():
            for key in VALUES:
                if VALUES[key] == letter:
                    word += key
        else:
            word += letter
    return word
