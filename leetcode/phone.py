def letter_combinations(digits):
    if not digits:
        return []

    # Mapping of digits to letters
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    # Start with an empty combination
    combinations = ['']

    for digit in digits:
        # Get the letters that the current digit maps to
        possible_letters = phone_map[digit]
        # Create new combinations by appending each letter to existing combinations
        combinations = [prev + letter for prev in combinations for letter in possible_letters]

    return combinations


# Example usage:
print(letter_combinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations(""))  # Output: []
print(letter_combinations("2"))  # Output: ["a","b","c"]