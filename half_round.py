def half_round(n):
    numbers = str(n).split('.')
    decimal = float(numbers[1][0] + '.' + numbers[1][1:])
    if 0 < decimal < 2.5:
        return float(numbers[0])
    elif 2.5 <= decimal < 7.5:
        return float(numbers[0] + '.5')
    elif 7.5 <= decimal:
        return float(numbers[0]) + 1

# return round(2 * n) / 2


print(half_round(8.8))
