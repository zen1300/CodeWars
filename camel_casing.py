def camel_casing(s):
    word = ''
    for letter in s:
        if letter.isupper():
            word += ' '
        word += letter
    return word
