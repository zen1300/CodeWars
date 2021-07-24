import re


def increment_string(strng):
    try:
        pattern = "\d+"
        match = re.findall(pattern, strng)
        num = match[-1]
        num_len = len(num)
        increment = int(num) + 1
        strng = strng[:-num_len] + str(increment).zfill(num_len)
    except (IndexError, AttributeError):
        strng = strng + '1'
    return strng


print(increment_string('k|7~gC#n"830Hdo:Y259567Eo!93766Y]400010'))
print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar1"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string(""))

