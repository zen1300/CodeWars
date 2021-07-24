from codewars_test import test_framework as Test
import itertools

def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None
    towns = itertools.combinations(ls, k)
    distances = [sum(i) for i in towns]
    diff = [i for i in distances if t >= i]
    if diff:
        return max(diff)
    else:
        return None



Test.it("Bigger numbers")
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
Test.assert_equals(choose_best_sum(230, 4, xs), 230)
Test.assert_equals(choose_best_sum(430, 5, xs), 430)

Test.assert_equals(choose_best_sum(430, 8, xs), None)
