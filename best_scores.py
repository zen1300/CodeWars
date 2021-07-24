def best_match(goals1, goals2):
    for index, (g1, g2) in enumerate(zip(goals1, goals2)):
        if index == 0:
            best2 = g2
            best_diff = g2 - g1
            best_index = index
        diff = g2 - g1
        if diff > best_diff:
            best_diff = diff
            best_index = index
            best2 = g2

        if diff == best_diff and g2 > best2:
            best_index = index
            best2 = max(best2, g2)
    return best_index


print(best_match([6, 4], [1, 2]))
print(best_match([1], [0]))
print(best_match([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(best_match([3, 4, 3], [1, 1, 2]))
print(best_match([4, 3, 4], [1, 1, 1]))
print(best_match([20, 3, 12, 1, 15, 5, 7, 14, 10, 17, 11], [10, 1, 8, 0, 6, 3, 1, 8, 9, 8, 4]))