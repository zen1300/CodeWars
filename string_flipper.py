def _get_counts(word):
    counts = {}
    word = word.lower()
    for letter in word:
        if letter not in counts:
            counts[letter] = word.count(letter)
    return counts


def _flip_string(word, counts):
    flipped = ''
    for letter in word:
        if letter.lower() in counts and counts[letter.lower()] % 2 != 0:
            flipped += letter.swapcase()
        else:
            flipped += letter

    return flipped


def work_on_strings(a, b):
    counts = _get_counts(b)
    flipped = _flip_string(a, counts)

    counts = _get_counts(a)
    flipped += _flip_string(b, counts)

    return flipped


print(work_on_strings("abc","cde"))
print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"))
print(work_on_strings("abcdeFg", "defgG"))
print(work_on_strings("abab", "bababa"))