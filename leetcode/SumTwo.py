import numbers


def sum_two_integers_arrays(nums, target):
    number_of_arrays = {}
    for index, num in enumerate(nums):
        result = target - num
        if result in number_of_arrays:
            return [number_of_arrays[result], index]
        number_of_arrays[result] = index
newNumbers = [2, 7, 11, 15]
newTarget = 9
print(sum_two_integers_arrays(newNumbers, newTarget))






