"""Phone inventory vol 2."""


def add_phone_quantity(phone_info: tuple, update: tuple) -> tuple:
    """
    Update tuple, if updated data brand and model exist.

    Given a tuple containing a phone brand, its models, and quantities,
    and an update tuple, return the updated data or empty tuple if brand and/or model doesn't exist.
    """
    brand1, models1, quanity1 = phone_info
    brand2, model2, quanity2 = update

    if brand1 == brand2 and model2 in models1:
        where = models1.index(model2)
        # print("where", where)
        total = quanity1[where] + quanity2
        # print("total", total)
    else:
        return ()

    return (brand1, models1, tuple([total if i == where else q for i, q in enumerate(quanity1)]))


def highest_quantity_brand(phones: list[tuple]) -> str:
    """
    Find brand with most models.

    Given a tuple containing phone brand data, return the brand with the highest total quantity of models.
    If there is a tie, return the one that appears first in the input list.
    """
    if not phones:
        return ''
    maks = max(thing[2] for thing in phones)
    for thing in phones:
        # print("MMM", thing[2])
        # several thing[2]
        # print("HEHE", sum(thing[2]))
        # print("MAKS", sum(maks))
        if maks == thing[2]:
            return thing[0]
        elif sum(maks) == sum(thing[2]):
            return thing[0]
    return ''


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    """
    hello = ''
    for a in phone_list:
        # print(a[0])
        for b in a[1]:
            hello += a[0] + " " + b + ","
            # print("b", b)
    return hello.strip()[:-1]


if __name__ == '__main__':
    print(add_phone_quantity(("Apple", ["iPhone 11", "iPhone 12"], (500, 300)),
                             ("Apple", "iPhone 11", 1)))
    # ("Apple", ["iPhone 11", "iPhone 12"], (501, 300))

    print(add_phone_quantity(("Apple", ["iPhone 11", "iPhone 12"], (500, 300)), ("Nokia", "3310", 10)))
    # ()

    print(highest_quantity_brand([("Apple", ["iPhone 11", "iPhone 12"], (500, 300)),
                                  ("Samsung", ["Galaxy S20", "Galaxy S21"], (600, 400)),
                                  ("Google", ["Pixel 4", "Pixel 5"], (200, 100))]))
    # Samsung

    print(highest_quantity_brand([("Apple", ["iPhone 11", "iPhone 12"], (100, 50)),
                                  ("Samsung", ["Galaxy S20", "Galaxy S21"], (110, 40)),
                                  ("Google", ["Pixel 4", "Pixel 5"], (70, 30))]))
    # Apple

    print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))
    # IPhone 11,Google Pixel
    print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))
    # IPhone 11,Google Pixel
    print(phone_list_as_string([['HTC', ['one', 'two']]]))
    # HTC one
