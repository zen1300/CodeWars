import operator

def zero(func=None):
    if func is not None:
        return func[0](0, func[1])
    else:
        return 0


def one(func=None):
    if func is not None:
        return func[0](1, func[1])
    else:
        return 1


def two(func=None):
    if func is not None:
        return func[0](2, func[1])
    else:
        return 2


def three(func=None):
    if func is not None:
        return func[0](3, func[1])
    else:
        return 3


def four(func=None):
    if func is not None:
        return func[0](4, func[1])
    else:
        return 4


def five(func=None):
    if func is not None:
        return func[0](5, func[1])
    else:
        return 5


def six(func=None):
    if func is not None:
        return func[0](6, func[1])
    else:
        return 6


def seven(func=None):
    if func is not None:
        return func[0](7, func[1])
    else:
        return 7


def eight(func=None):
    if func is not None:
        return func[0](8, func[1])
    else:
        return 8


def nine(func=None):
    if func is not None:
        return func[0](9, func[1])
    else:
        return 9


def plus(value):
    return (operator.add, value)


def minus(value):
    return (operator.sub, value)


def times(value):
    return (operator.mul, value)


def divided_by(value):
    return (operator.floordiv, value)


print(seven(times(five())))
