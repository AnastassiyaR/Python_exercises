def add_two_numbers(l1, l2):
    result = []
    check = 0
    maxlength = max(len(l1), len(l2))
    print('a', maxlength)
    for i in range(maxlength):
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[i] if i < len(l2) else 0
        print(val1, val2)
        total = val1 + val2 + check
        check = total // 10
        result.append(total % 10)

    if check:
        result.append(check)

    return result



# Example usage:
print(add_two_numbers([2, 4, 3], [5, 6, 4]))  # Output: [7, 0, 8]
# print(add_two_numbers([0], [0]))  # Output: [0]
# print(add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]