"""
Starting to organize algs
"""


def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        index = j - 1
        while index >= 0 and array[index] > key:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = key
    return array


def maximum_subarray(array):
    pass

if __name__ == "__main__":
    test_array = [3, 1, 5, 7, 2, 4]
    print(insertion_sort(test_array))