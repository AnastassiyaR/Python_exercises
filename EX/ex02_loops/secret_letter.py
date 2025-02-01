"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.
    print(secret_letter("anotherVALIDLETTER17"))  # True


    :param letter: secret letter
    :return: validation
    """
    uppercase = ""
    lowercase = ""
    sum = 0
    for x in letter:
        if x.isalpha() and x.isupper():
            uppercase += x
        if x.isalpha() and x.islower():
            lowercase += x
        if x.isdigit():
            sum += int(x)
    print(uppercase, lowercase, sum)
    print(len(lowercase), len(uppercase), sum)
    if len(lowercase) < len(uppercase) and sum <= len(uppercase) and sum >= len(lowercase):
        return True
    else:
        return False


if __name__ == '__main__':
    print(secret_letter("anotherVALIDLETTER17"))  # True
