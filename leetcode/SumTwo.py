def sum_two_integers_arrays(nums, target):
    number_of_arrays = {}
    for index, num in enumerate(nums):
        result = target - num
        if result in number_of_arrays:
            return [number_of_arrays[result], index]
        else:
            number_of_arrays[result] = index

newNumbers = [7,9,3,9]
newTarget = 9
print(sum_two_integers_arrays(newNumbers, newTarget))






