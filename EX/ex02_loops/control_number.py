"""Control number."""


def control_number(encrypted_string: str) -> bool:
    """
    Given encrypted string that has a control number in the end of it, return True if correct, else False.

    Calculating the correct control number:
    1. Start the calculation from 0.
    2. Add 1 for every lowercase occurrence.
    3. Add 2 for every uppercase occurrence.
    4. Add 5 for any of the following symbol occurrences: "?!@#".
    Other symbols/letters/digits don't affect the result.

    NB! If for example the number you come up with is 25, you only have to check the last two digits of the string.
    e.g. control_number("?!?!#4525") -> True, because it ends with 25.

    :param encrypted_string: encrypted string
    :return: validation
    """
    result = 0
    symbol = ['?', '!', '@', '#']
    # Find the number
    for x in encrypted_string:
        if x.isalpha() and x.isupper():
            result += 2
        elif x.isalpha() and x.islower():
            result += 1
        elif x in symbol:
            result += 5
        else:
            result += 0
    # print("r", result)

    # Control True or False
    # Quanity of number (result)
    digit_quantity = 0
    for i in str(result):
        digit_quantity += 1
    # print("d", digit_quantity)

    # Find number
    from_number = -1 * digit_quantity
    # print("f", from_number)

    control = encrypted_string[from_number:]
    # print("control", control)

    # CHECK
    # print(control, result)
    # panna str() since "r9"
    if str(control) == str(result):
        return True
    else:
        return False


if __name__ == '__main__':
    print(control_number("mE0W5"))  # True
    print(control_number("SomeControlNR?20"))  # False
    print(control_number("False?Nr9"))  # False
    print(control_number("#Hello?!?26"))  # True
    print(control_number("3423982340000000.....///....0"))  # True
    print(control_number("#Shift6"))  # False
