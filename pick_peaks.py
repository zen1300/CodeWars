from codewars_test import test_framework as Test


def pick_peaks(arr):
    peaks = []
    pos = []
    for index, value in enumerate(arr):
        if 0 < index < len(arr) - 1:
            if arr[index - 1] < arr[index] >= arr[index + 1]:
                if arr[index] == arr[index + 1]:
                    for i in range(index, len(arr)):
                        if arr[index] > arr[i]:
                            peaks.append(arr[index])
                            pos.append(index)
                            break
                        elif arr[index] < arr[i]:
                            break
                else:
                    peaks.append(arr[index])
                    pos.append(index)

    return {'pos': pos, 'peaks': peaks}


Test.assert_equals(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})
Test.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})
Test.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10], "peaks": [6, 3, 2]})
Test.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})
Test.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
Test.assert_equals(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), {"pos": [2], "peaks": [3]})
Test.assert_equals(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]), {"pos": [2], "peaks": [3]})
Test.assert_equals(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]),
                   {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
Test.assert_equals(pick_peaks([]), {"pos": [], "peaks": []})
Test.assert_equals(pick_peaks([1, 1, 1, 1]), {"pos": [], "peaks": []})
