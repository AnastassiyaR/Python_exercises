def length_of_longest_substring(s: str) -> int:
    result = []
    max_length = 0
    start = 0

    for i in range(len(s)):
        if s[i] not in result:
            result.append(s[i])
        else:
            # If we find a duplicate, we need to remove characters from the start
            while s[start] != s[i]:
                result.remove(s[start])
                start += 1
            # Move start one step further to remove the duplicate character
            start += 1
            # print(result, start)
        max_length = max(max_length, i - start + 1)

    return max_length


    #print(result)
# Example usage:
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3
