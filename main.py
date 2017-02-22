from algorithms import SearchAlgorithms, SortAlgorithms

test_values = [
    8661, -22345, -31557, -22213, 11852, -13914, -17491, 18370, 30381, -31439, 15413, -1278, -19079,
    -7457, 31067, -25552, 10519, 27118, 28254, 934, -23623, 17375, -12449, 27817, -27437, -25998,
    16675, -861, -18694, -23428, -25818, 16120, 24028, 10450, -30052, 6200, -12086, 29651, -1577,
    20240, -24437, 13898, -16980, -21218, -13496, -23156, 14168, -10327, 14284, -9276, -8978, 25956,
    -3284, 13187, -9220, 7746, 3525, -9444, 13322, 5374, 23258, -13029, 20698, 14288, -9584, 11985,
    -102, 24557, -3426, 11545, 17138, -10272, 30170, 18561, 28307, 5238, -5147, -17016, -383, -13659,
    -28072, 17228, -8349, -14905, 28689, -11458, 19832, 25715, 23377, 20625, 10474, -27003, 22487,
    -30254, 8555, 5611, 5409, -25634, -12081, -30298
]

test_values_short = [2, -1, 0, 3, -3, 1, -2]

max_array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

search = SearchAlgorithms()
sort = SortAlgorithms()

# sorted_values = sort.linear_sort(test_values)
sorted_values = sort.merge_manager(test_values_short, 0, 6)

print(search.find_max_subarray(max_array, 0, 15))
# print array to confirm sorting
print_line = []
for k in range(len(sorted_values)):
    print_line.append(sorted_values[k])
    if (k + 1) % 15 == 0:
        print(", ".join([str(x) for x in print_line]))
        print_line.clear()
print(", ".join([str(x) for x in print_line]))