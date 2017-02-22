import math


# class GeneralAlgorithms:


class SearchAlgorithms:

    @staticmethod
    def linear_search(target, array):
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1

    def find_max_subarray(self, array, start, end):
        if start >= end:
            return {"left": start, "right": end, "sum": array[start]}
        mid = start + (end - start) // 2
        left_subarray = self.find_max_subarray(array, start, mid)
        right_subarray = self.find_max_subarray(array, mid + 1, end)
        crossing_subarray = self.find_max_crossing_subarray(array, start, mid, end)

        if left_subarray['sum'] >= right_subarray['sum'] and left_subarray['sum'] >= crossing_subarray['sum']:
            return left_subarray
        elif right_subarray['sum'] >= left_subarray['sum'] and right_subarray['sum'] >= crossing_subarray['sum']:
            return right_subarray
        else:
            return crossing_subarray

    @staticmethod
    def find_max_crossing_subarray(array, start, mid, end):
        left_index = mid
        right_index = mid
        left_sum = -math.inf
        right_sum = -math.inf

        sum = 0
        for i in range(mid, start, -1):
            sum += array[i]
            if sum > left_sum:
                left_sum = sum
                left_index = i

        sum = 0
        for j in range(mid + 1, end):
            sum += array[j]
            if sum > right_sum:
                right_sum = sum
                right_index = j

        return {"left": left_index, "right": right_index, "sum": left_sum + right_sum}


class SortAlgorithms:

    @staticmethod
    def linear_sort(array):
        for j in range(1, len(array)):
            key = array[j]
            i = j - 1
            while i >= 0 and array[i] > key:
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key
        return array
    
    def insertion_sort(array):
        for j in range(1, len(array)):
            key = array[j]
            index = j - 1
            while index >= 0 and array[index] > key:
                array[index + 1] = array[index]
                index -= 1
            array[index + 1] = key
        return array

    def merge_manager(self, array, start, end):
        if (end - start) > 0:
            middle = (start + end) // 2
            self.merge_manager(array, start, middle)
            self.merge_manager(array, middle + 1, end)
            self.merge_sort(array, start, middle, end)
        return array

    @staticmethod
    def merge_sort(array, start, middle, end):
        results = []
        n_sub1 = middle - start + 1
        n_sub2 = end - middle

        first_half = []
        second_half = []

        # fill the subarrays from the original array
        for i in range(n_sub1):
            first_half.append(array[start + i])
        for i in range(n_sub2):
            second_half.append(array[start + i + n_sub1])

        # add end of array markers
        first_half.append(math.inf)
        second_half.append(math.inf)

        first_subarray_index = 0
        second_subarray_index = 0

        for i in range(end - start + 1):
            first_half_value = first_half[first_subarray_index]
            second_half_value = second_half[second_subarray_index]

            if first_half_value <= second_half_value:
                array[start + i] = first_half_value
                first_subarray_index += 1
            else:
                array[start + i] = second_half_value
                second_subarray_index += 1
        return results
