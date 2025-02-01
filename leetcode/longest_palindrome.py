def longest_palindrome(s: str) -> str:
    result = ''
    end = len(s) - 1
    start = 0
    if len(s) < 1:
        return ""

    for i in range(len(s)):
        if s[start] != s[end]:
            start += 1
            end -= 1
        elif s[start] == s[end]:
            result += s[start]
            start += 1
            end -= 1
        elif s[i] == s[len(s) // 2]:
            result += s[i]

    return result


print(longest_palindrome("babad"))  # Output: "bab" or "aba"
print(longest_palindrome("cbbd"))  # Output: "bb"