"""Inflation."""


def inflation(n: int, goal: int) -> int:
    """
    Increase the given positive number until it reaches the goal (or goes over it).

    NB! The number must be returned the first time it reaches the goal or goes over it (don't increase it more).
    NB! The number is increased only once per cycle iteration:
    if it gains an extra digit within the cycle, it should not be increased again until the next cycle iteration.

    Rules:
    1. If the number is exactly 1/2 of the goal, multiply it by 2. (Most important)
    2. If the number is currently a 1-digit number, multiply it by 5.
    3. If the number is currently a 2-digit number, multiply it by 4.
    4. If the number is currently a 3-digit number, multiply it by 3.
    5. If the number is currently a 4-digit number, multiply it by 2.
    6. In any other case, multiply it by 7.

    :param n: starting number
    :param goal: goal to reach (may go over)
    :return: new number
    """
    result = n

    if goal / 2 == n:
        result *= 2
    # print("r", result)

    while goal > result < 10:
        # print("checkn1", n)
        # The first number and result is 0
        result *= 5
        # print("check1", result)
    # print("r1", result)

# If the number is currently 2-digit number, multiply it by 4.
    while goal > result < 100:
        # print("checkn2", n)
        result *= 4
        # print("check2", result)
    # print("r2", result)

# If the number is currently a 3-digit number, multiply it by 3.
    while goal > result < 1000:
        # print("checkn3", n)
        result *= 3
        # print("check3", result)
    # print("r3", result)

# If the number is currently a 4-digit number, multiply it by 2.
    while goal > result < 10000:
        # print("checkn4", n)
        result *= 2
        # print("check4", result)
    # print("r4", result)

# In any other case, multiply it by 7.
    if result >= 10000:
        while goal > result:
            # print("checkn77", n)
            result *= 7
            # print("check77", result)
    return result


if __name__ == '__main__':
    print(inflation(10, 11))  # 40
    print(inflation(2, 1000))  # 1440
    print(inflation(800, 79400))  # 134400
    print(inflation(2, 5784))  # 11520
    print(inflation(39, 3400))  # 5616
    print(inflation(5, 10))  # 10
