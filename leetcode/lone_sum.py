def lone_sum(*args):
    # Create a dictionary to count occurrences of each number
    counts = {}

    # Count each number's occurrences
    for num in args:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Calculate the sum of numbers that appear only once
    total = sum(num for num, count in counts.items() if count == 1)

    return total


# Example usage
print(lone_sum(1, 2, 3))  # Output: 6
print(lone_sum(3, 2, 3))  # Output: 2
print(lone_sum(3, 3, 3))  # Output: 0
print(lone_sum(1, 2, 2, 3, 4))  # Output: 8 (1 + 3 + 4)
print(lone_sum(1, 1, 2, 3, 3, 4))  # Output: 4 (4 is the only unique number)