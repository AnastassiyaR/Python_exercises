def is_valid(s: str) -> bool:
    # Dictionary to hold matching pairs
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the topmost element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped bracket matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack

# Example usage:
print(is_valid("()"))          # Output: True
print(is_valid("()[]{}"))      # Output: True
print(is_valid("(]"))          # Output: False
print(is_valid("([)]"))        # Output: False
print(is_valid("{[]}"))        # Output: True