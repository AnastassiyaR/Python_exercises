def sort_descending(nums):
    return sorted(nums, reverse=True)

# Example usage
print(sort_descending([1, 2, 3]))             # Output: [3, 2, 1]
print(sort_descending([5, 11, 9]))            # Output: [11, 9, 5]
print(sort_descending([7, 0, 0]))             # Output: [7, 0, 0]
print(sort_descending([1, 2, 3, 4, 5]))       # Output: [5, 4, 3, 2, 1]
print(sort_descending([10, 20, 30, 40, 50]))  # Output: [50, 40, 30, 20, 10]
print(sort_descending([]))                     # Output: []