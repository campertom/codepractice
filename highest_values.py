# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

# gracie's algorithm
# max() and min() are python methods for finding high and low values
# sort()
# my algorithm
# lookup list methods specific to high values


# def two_highest(arg1):
#     copy_of_arg1 
#     sorted = sort(arg1)
#     largest = max(copy_of_arg1)
#     copy_of_arg1.remove(largest_arg1) 
# two_highest([1,2,3,4])
def two_highest(integers):
# clone the list by slicing
    copy_of_integers = integers[:]  # [1, 16, 3, 39, 26, 4, 8, 16]

    largest_integer = max(copy_of_integers)  # 39
    copy_of_integers.remove(largest_integer)

    second_largest_integer = max(copy_of_integers)
    return copy_of_integers
print(two_highest([1, 16, 3, 39, 26, 4, 8, 16]))