"""Some cool pyramids."""


def create_simple_pyramid_left(height: int) -> str:
    """
    Create simple pyramid on the left side.

    *
    **
    ***
    ****

    Use recursion!
    # '' + '*' == '*' , save the result after calculation

    :param height: Pyramid height.
    :return: Pyramid.
    """
    if height == 0:
        return ''
    else:
        return create_simple_pyramid_left(height - 1) + ('\n' if height > 1 else '') + '*' * height
    # create_simple_pyramid_left(height - 1) превращается в ''


def create_simple_pyramid_right(height: int, current=0) -> str:
    """
    Create simple pyramid on the right side.

       *
      **
     ***
    ****

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if height == 0:
        return ''

    space = ' ' * current
    stars = '*' * height

    return create_simple_pyramid_right(height - 1, current + 1) + ('\n' if height > 1 else '') + space + stars


def create_number_pyramid_left(height: int, current=1) -> str:
    """
    Create left-aligned number pyramid.

    1
    21
    321
    4321

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    return ''.join(str(i) for i in range(1, current + 1)) + "\n" + create_number_pyramid_left(height, current + 1)


def create_number_pyramid_right(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid.

        1
       21
      321
     4321

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    space = ' ' * (height - current)

    return space + ''.join(str(i) for i in range(current, 0, -1)) + '\n' + create_number_pyramid_right(height, current + 1)


def create_number_pyramid_left_down(height: int, current=1) -> str:
    """
    Create left-aligned number pyramid upside-down.

    4321
    321
    21
    1

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    return ''.join(str(i) for i in range(height - current + 1, 0, -1)) + "\n" + create_number_pyramid_left_down(height, current + 1)
    #  '1'+'\n'


def create_number_pyramid_right_down(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid upside-down.

    1234
     123
      12
       1

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    space = ' ' * (current - 1)
    numbers = ''.join(str(i) for i in range(1, height - current + 2))  # Числа от 1 до (height - current + 2) 2 because 2 ^^

    return space + numbers + '\n' + create_number_pyramid_right_down(height, current + 1)


def create_regular_pyramid(height: int, current=1) -> str:
    """
    Create regular pyramid.

       *
      ***
     *****
    *******

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ''

    spaces = " " * (height - current)
    stars = "*" * (2 * current - 1)
    return spaces + stars + "\n" + create_regular_pyramid(height, current + 1)


def create_regular_pyramid_upside_down(height: int, current=1) -> str:
    """
    Create regular pyramid upside down.

    *******
     *****
      ***
       *

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = " " * (current - 1)
    stars = "*" * (2 * (height - current + 1) - 1)

    return spaces + stars + "\n" + create_regular_pyramid_upside_down(height, current + 1)


def create_diamond(height: int, current=1) -> str:
    """
    Create diamond.

       *
      ***
     *****
    *******
    *******
     *****
      ***
       *

    Use recursion!

    :param height: Height of half of the diamond.
    :param current: Keeping track of current layer.
    :return: Diamond.
    """
    if current > height:
        return create_regular_pyramid_upside_down(height)

    spaces = " " * (height - current)
    stars = "*" * (2 * current - 1)
    return spaces + stars + "\n" + create_diamond(height, current + 1)


def create_empty_pyramid(height: int, current=1) -> str:
    """
    Create empty pyramid.

       *
      * *
     *   *
    *******

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""
    elif current == height:
        return "*" * (2 * height - 1) + "\n" + create_empty_pyramid(height, current + 1)  # отвечает за нижнюю часть

    spaces = " " * (height - current)
    if current == 1:
        return spaces + "*" + "\n" + create_empty_pyramid(height, current + 1)  # это для верхушки
    else:
        return spaces + "*" + " " * (2 * current - 3) + "*" + "\n" + create_empty_pyramid(height, current + 1)  # это за части с дырами


if __name__ == '__main__':
    print("\ncreate_simple_pyramid_left:")
    print("expected:\n*\n**\n***\n****")
    print(f"\ngot:\n{create_simple_pyramid_left(4)}")

    print("\ncreate_simple_pyramid_right:")
    print("expected:\n   *\n  **\n ***\n****")
    print(f"\ngot:\n{create_simple_pyramid_right(4)}")

    print("\ncreate_number_pyramid_left:")
    print("expected:\n1\n12\n123\n1234")
    print(f"\ngot:\n{create_number_pyramid_left(4)}")

    print("\ncreate_number_pyramid_right:")
    print("expected:\n   1\n  21\n 321\n4321")
    print(f"\ngot:\n{create_number_pyramid_right(4)}")

    print("\ncreate_number_pyramid_right_bigger_pyramid:")
    print("expected:\n          1\n         21\n        321\n"
          "       4321\n      54321\n     654321\n    7654321\n"
          "   87654321\n  987654321\n 10987654321\n1110987654321")
    print("Or expected:\n            1\n           21\n          321\n"
          "         4321\n        54321\n       654321\n      7654321\n"
          "     87654321\n    987654321\n  10987654321\n1110987654321")
    print(f"\ngot:\n{create_number_pyramid_right(11)}")

    print("\ncreate_number_pyramid_left_down:")
    print("expected:\n4321\n321\n21\n1")
    print(f"\ngot:\n{create_number_pyramid_left_down(4)}")

    print("\ncreate_number_pyramid_right_down:")
    print("expected:\n1234\n 123\n  12\n   1")
    print(f"\ngot:\n{create_number_pyramid_right_down(4)}")

    print("\ncreate_number_pyramid_right_down_bigger_pyramid:")
    print("expected:\n1234567891011\n 12345678910\n  123456789\n"
          "   12345678\n    1234567\n     123456\n      12345\n"
          "       1234\n        123\n         12\n          1")
    print("Or expected:\n1234567891011\n  12345678910\n    123456789\n"
          "     12345678\n      1234567\n       123456\n        12345\n"
          "         1234\n          123\n           12\n            1")
    print(f"\ngot:\n{create_number_pyramid_right_down(11)}")

    print("\ncreate_regular_pyramid:")
    print("expected:\n   *\n  ***\n *****\n*******")
    print(f"\ngot:\n{create_regular_pyramid(4)}")

    print("\ncreate_regular_pyramid_upside_down:")
    print("expected:\n*******\n *****\n  ***\n   *")
    print(f"\ngot:\n{create_regular_pyramid_upside_down(4)}")

    print("\ncreate_diamond:")
    print("expected:\n   *\n  ***\n *****\n*******\n*******\n *****\n  ***\n   *")
    print(f"\ngot:\n{create_diamond(4)}")

    print("\ncreate_empty_pyramid:")
    print("expected:\n   *\n  * *\n *   *\n*******")
    print(f"\ngot:\n{create_empty_pyramid(4)}")
